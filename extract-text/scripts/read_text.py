#!/usr/bin/env python3
"""
read_text.py: pull the words out of pictures and PDFs.

Handles a single image, a folder of images, a PDF that already carries text,
a PDF that is only scanned pictures, and a PDF that is a mix of both. It says
which of those it found, and it marks any word the reader was unsure about so
nobody copies a wrong number out of a scan.

Usage:
    python3 read_text.py --check
    python3 read_text.py invoice.png
    python3 read_text.py report.pdf --out report.txt
    python3 read_text.py ./screenshots/ --out-dir ./text/
    python3 read_text.py hindi-page.jpg --lang hin+eng
    python3 read_text.py scan.pdf --no-flags      # plain text, no [?] marks
"""

import argparse
import csv
import glob
import io
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp", ".gif", ".heic"}

# Below this score, tesseract is guessing. 60 is where its own docs put the line
# between "confident" and "worth a human glance".
LOW_CONFIDENCE = 60

# A page with fewer real words than this is treated as a picture of a page
# rather than a page of text.
TEXT_LAYER_MIN_WORDS = 12


# ---------------------------------------------------------------- dependencies

TOOLS = {
    "tesseract": "the reader itself, the part that turns pixels into letters",
    "pdftotext": "lifts text straight out of a PDF that already has some",
    "pdftoppm": "turns a PDF page into a picture so it can be read",
}

INSTALL_HINT = """
Install what is missing, then run this again:

    macOS      brew install tesseract poppler
    Ubuntu     sudo apt install tesseract-ocr poppler-utils
    Windows    winget install UB-Mannheim.TesseractOCR
               winget install oschwartz10612.Poppler

tesseract is one package. pdftotext and pdftoppm both live inside poppler,
so one install covers both.
"""


def check_tools(needed):
    missing = [t for t in needed if shutil.which(t) is None]
    return missing


def cmd_check():
    print("Checking what is installed.\n")
    missing = []
    for tool, why in TOOLS.items():
        path = shutil.which(tool)
        if path:
            print(f"  found    {tool:<12} {why}")
        else:
            print(f"  MISSING  {tool:<12} {why}")
            missing.append(tool)
    if missing:
        print(INSTALL_HINT)
        return 1
    langs = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True)
    installed = [l for l in langs.stdout.splitlines()[1:] if l.strip()]
    print(f"\n  languages available: {', '.join(installed) if installed else 'eng'}")
    print("\nEverything needed is here.")
    return 0


# ---------------------------------------------------------------- reading images

def read_image(path, lang="eng", psm="3", flag_unsure=True):
    """Read one picture. Returns (text, total_words, unsure_words)."""
    proc = subprocess.run(
        ["tesseract", str(path), "stdout", "-l", lang, "--psm", psm, "tsv"],
        capture_output=True,
    )
    rows = proc.stdout.decode("utf-8", errors="replace").splitlines()
    if len(rows) < 2:
        return "", 0, 0

    reader = csv.DictReader(io.StringIO("\n".join(rows)), delimiter="\t",
                            quoting=csv.QUOTE_NONE)
    lines, current, last_key = [], [], None
    total = unsure = 0

    for row in reader:
        word = (row.get("text") or "").strip()
        if not word:
            continue
        try:
            conf = float(row.get("conf", -1))
        except ValueError:
            conf = -1
        key = (row.get("block_num"), row.get("par_num"), row.get("line_num"))
        if last_key is not None and key != last_key:
            lines.append(" ".join(current))
            current = []
            if key[0] != last_key[0]:
                lines.append("")
        last_key = key
        total += 1
        if 0 <= conf < LOW_CONFIDENCE:
            unsure += 1
            if flag_unsure:
                word += "[?]"
        current.append(word)

    if current:
        lines.append(" ".join(current))
    return "\n".join(lines).strip(), total, unsure


# ---------------------------------------------------------------- reading PDFs

def page_count(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    # pdfinfo is optional; fall back to rendering probe
    return 0


def page_text_layer(pdf, page):
    out = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"],
        capture_output=True, text=True, errors="replace",
    ).stdout
    return out.strip()


def read_pdf(pdf, lang="eng", dpi=300, flag_unsure=True, progress=True):
    """
    Walk the PDF page by page. A page that already carries text is copied
    straight out, which is why some files finish in seconds. A page that is a
    picture has to be rendered and read, which is the slow part.
    """
    pages = page_count(pdf)
    if not pages:
        pages = 10000  # keep going until pdftoppm runs out

    chunks = []
    lifted = scanned = 0
    total = unsure = 0

    with tempfile.TemporaryDirectory() as work:
        for page in range(1, pages + 1):
            layer = page_text_layer(pdf, page)
            if layer and len(layer.split()) >= TEXT_LAYER_MIN_WORDS:
                chunks.append(layer)
                total += len(layer.split())
                lifted += 1
            else:
                prefix = os.path.join(work, f"p{page:05d}")
                render = subprocess.run(
                    ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                     "-gray", "-png", str(pdf), prefix],
                    capture_output=True,
                )
                images = sorted(glob.glob(prefix + "*.png"))
                if not images:
                    if render.returncode != 0 and page > 1:
                        break  # ran past the end of the file
                    continue
                text, words, low = read_image(images[0], lang=lang,
                                              flag_unsure=flag_unsure)
                chunks.append(text)
                total += words
                unsure += low
                scanned += 1
                for image in images:
                    os.remove(image)

            if progress and page % 10 == 0:
                print(f"    page {page}: {total:,} words so far", flush=True)

    kind = ("text" if scanned == 0 else
            "scanned" if lifted == 0 else "mixed")
    return "\n\n".join(c for c in chunks if c), {
        "words": total, "unsure": unsure,
        "pages_lifted": lifted, "pages_read": scanned, "kind": kind,
    }


# ---------------------------------------------------------------- driving it

def gather(target):
    p = Path(target)
    if p.is_dir():
        files = [f for f in sorted(p.iterdir())
                 if f.suffix.lower() in IMAGE_TYPES or f.suffix.lower() == ".pdf"]
        return files
    if any(ch in str(target) for ch in "*?["):
        return [Path(f) for f in sorted(glob.glob(str(target)))]
    return [p]


def plural(n, word):
    return word if n == 1 else word + "s"


def describe(stats):
    if "kind" not in stats:
        return "picture"
    return {
        "text": "a PDF that already had its text, lifted straight out",
        "scanned": (f"a scanned PDF, {stats['pages_read']} "
                    f"{plural(stats['pages_read'], 'page')} read as pictures"),
        "mixed": (f"a mixed PDF, {stats['pages_lifted']} "
                  f"{plural(stats['pages_lifted'], 'page')} had text already and "
                  f"{stats['pages_read']} had to be read as pictures"),
    }[stats["kind"]]


def run_one(path, out_path, lang, dpi, flag_unsure):
    if not path.exists():
        print(f"  cannot find {path}")
        return None
    print(f"\n{path.name}")
    if path.suffix.lower() == ".pdf":
        text, stats = read_pdf(path, lang=lang, dpi=dpi, flag_unsure=flag_unsure)
    else:
        text, words, low = read_image(path, lang=lang, flag_unsure=flag_unsure)
        stats = {"words": words, "unsure": low}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text or "", encoding="utf-8")

    print(f"  {describe(stats)}")
    print(f"  {stats['words']:,} words -> {out_path}")
    if stats["unsure"]:
        share = stats["unsure"] * 100 / max(stats["words"], 1)
        mark = " marked [?] in the text" if flag_unsure else ""
        print(f"  {stats['unsure']:,} {plural(stats['unsure'], 'word')} the reader "
              f"was unsure about ({share:.1f}%){mark}")
    read_pages = stats.get("pages_read", 0)
    if stats["words"] < 5:
        print("  barely anything came out. The file may be locked, blank, "
              "or a picture with no words in it.")
    elif read_pages and stats["words"] / read_pages < 10:
        print("  very few words per page. The scan may be too faint or too "
              "small. Try --dpi 400.")
    return stats


def main():
    ap = argparse.ArgumentParser(description="Get the words out of pictures and PDFs.")
    ap.add_argument("target", nargs="?", help="a file, a folder, or a pattern like '*.png'")
    ap.add_argument("--out", help="where to write the text for a single file")
    ap.add_argument("--out-dir", default=".", help="where to write text for a folder")
    ap.add_argument("--lang", default="eng",
                    help="language, e.g. eng, deu, hin+eng (default eng)")
    ap.add_argument("--dpi", type=int, default=300,
                    help="how finely to render PDF pages (default 300; try 400 on small print)")
    ap.add_argument("--no-flags", action="store_true",
                    help="leave out the [?] marks on uncertain words")
    ap.add_argument("--check", action="store_true",
                    help="report what is installed and what is missing")
    args = ap.parse_args()

    if args.check:
        sys.exit(cmd_check())
    if not args.target:
        ap.error("give me a file, a folder, or --check")

    needed = ["tesseract"]
    if str(args.target).lower().endswith(".pdf") or Path(args.target).is_dir():
        needed += ["pdftotext", "pdftoppm"]
    missing = check_tools(needed)
    if missing:
        print("Cannot start. These are not installed: " + ", ".join(missing))
        print(INSTALL_HINT)
        sys.exit(1)

    files = gather(args.target)
    if not files:
        print(f"Nothing to read at {args.target}")
        sys.exit(1)

    flag = not args.no_flags
    if len(files) == 1 and args.out:
        run_one(files[0], Path(args.out), args.lang, args.dpi, flag)
        return

    out_dir = Path(args.out_dir)
    done = words = unsure = 0
    for f in files:
        stats = run_one(f, out_dir / (f.stem + ".txt"), args.lang, args.dpi, flag)
        if stats:
            done += 1
            words += stats["words"]
            unsure += stats["unsure"]

    if len(files) > 1:
        print(f"\n{done} of {len(files)} files read, {words:,} words in total.")
        if unsure:
            print(f"{unsure:,} of those carry a [?] and want a human glance.")


if __name__ == "__main__":
    main()
