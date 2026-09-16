---
name: extract-text
description: >
  Get the words out of a picture or a PDF so they can be worked with as text. Use this whenever
  someone has something they can see but cannot select or copy: a screenshot of a dashboard or an
  error, a photo of a page in a book or a whiteboard, a scanned contract or invoice a client
  emailed, a slide deck sent as images, a folder of phone photos of receipts. It triggers on plain
  phrases as well as technical ones, including "get the text out of this", "my client sent a scan",
  "I can't copy from this PDF", "read what this screenshot says", "type up this photo for me",
  "turn these receipts into a spreadsheet I can use", "what does this say", and "OCR this".
  It also fits when a PDF refuses to give up its text, or when text copied out of one comes back
  empty or as gibberish. Do NOT use it for a PDF that already selects and copies cleanly, since
  reading that one directly is faster and exact. Do NOT use it to tidy up prose that is already
  text, which is make-it-readable, and do NOT use it to check that some other job really ran,
  which is prove-it.
allowed-tools: ["Bash", "Read", "Write"]
---

# read this

The useful thing is trapped in a picture. Someone has a screenshot, a photo of a page, a scan a
client emailed, and the numbers or the paragraphs inside it are the whole point. This skill lifts
them out as text, and it is honest about the parts it could not read confidently, because a wrong
figure copied out of a scanned invoice does more damage than no figure at all.

## Start here

`scripts/read_text.py` does the work. It ships with this skill so that nobody has to write the same
helper again, and so that the awkward parts, telling a real PDF from a scanned one, rendering pages
at the right size, scoring how sure the reader was of each word, behave the same way every time.

Before the first run on a machine, check what is installed:

```bash
python3 scripts/read_text.py --check
```

It names each missing piece and gives the one command that installs it. Read the next section
before running anything, because this is the step where people give up.

## What has to be installed, and what to do when it is not

Two free programs do the actual work. They are not Python packages and they do not come with
Claude Code, so they are installed once and then forgotten.

| Program | What it does here |
|---|---|
| tesseract | Turns pixels into letters. This is the reader. |
| poppler | Handles PDFs. It gives us `pdftotext`, which lifts text a PDF already has, and `pdftoppm`, which turns a PDF page into a picture that tesseract can read. One install, two tools. |

```bash
# macOS (installs Homebrew first if the brew command is not found)
brew install tesseract poppler

# Ubuntu or Debian Linux
sudo apt install tesseract-ocr poppler-utils

# Windows
winget install UB-Mannheim.TesseractOCR
winget install oschwartz10612.Poppler
```

If `brew` is not a recognised command on a Mac, Homebrew itself is missing. Install it with the one
line at https://brew.sh, close the terminal, open a new one, then run the `brew install` above. The
new terminal matters, because the old one does not know about a program installed after it started.

On Windows, `winget` sometimes finishes and the tools still are not found, which is almost always the
same thing: open a new terminal window and try `--check` again before assuming the install failed.

When a user hits a wall here, say plainly which single program is missing and what it is for. Being
stuck at an install with no idea what is missing is where this audience stops, and one sentence of
explanation is usually the whole fix.

## Running it

```bash
# one screenshot or photo
python3 scripts/read_text.py dashboard.png --out dashboard.txt

# a PDF of any kind
python3 scripts/read_text.py contract.pdf --out contract.txt

# a whole folder, one text file out per file in
python3 scripts/read_text.py ./receipts/ --out-dir ./receipts-text/

# something other than English
python3 scripts/read_text.py page.jpg --lang deu        # German
python3 scripts/read_text.py page.jpg --lang hin+eng    # Hindi mixed with English

# small print that came out poorly at the default size
python3 scripts/read_text.py fine-print.pdf --out fine.txt --dpi 400
```

A language pack has to be installed before `--lang` can use it: `brew install tesseract-lang` on
macOS, or `sudo apt install tesseract-ocr-deu` and friends on Linux. `--check` lists which ones are
already there.

## Say which kind of file it was

The script reports this and it is worth repeating back, because the same command can finish in
3 seconds or run for 3 minutes and a user who does not know why assumes something has broken.

- **A PDF that already has text.** Nothing is read, the text is simply lifted out. Nearly instant,
  and perfectly accurate.
- **A scanned PDF.** Every page is a photograph, so every page has to be rendered and read. Budget
  a second or two per page, more on a big book.
- **A mixed PDF.** Very common when someone signs a page and scans just that one back into a digital
  document. The script handles each page the right way on its own and tells you how many went each
  route.
- **A picture.** One screenshot or photo, read directly, usually under a second.

So when the wait is long, the reason is that there were 200 photographs of pages in there, not that
anything is wrong. Say so while it runs.

## Being honest about accuracy

Tesseract scores its own confidence in every word it reads. Any word it scored below 60 comes back
marked `[?]`, and the summary line says how many there were.

Those marks are the point of the skill. A blurry 8 read as a 3 is invisible in clean-looking text,
and it stays invisible until somebody acts on it. When a run comes back with flags:

1. Say how many there were and what share of the total that is. Eleven flagged words out of nine
   thousand is background noise. Eleven out of forty means the scan itself is poor.
2. Open the picture and look at the flagged spots. Claude can read the image directly, and for a few
   uncertain words that is the fastest correction there is. Fix them in the text file, and say which
   ones were changed.
3. Look hard at any flag sitting on a number, a date, a name, an account or an invoice total. Those
   are the ones that cost something when they are wrong. Prose usually survives a bad word. A figure
   does not.
4. If the flags are heavy, rerun with `--dpi 400`, which renders PDF pages larger and often clears
   up small or faint print. For a photo, a straighter, better-lit retake beats any setting.

`--no-flags` removes the marks when the text is headed somewhere the brackets would be a nuisance.
Only reach for it once the uncertain words have actually been checked.

## Finish with something in their hands

End on a real file, named after the thing it came from, in a place they can find, with the full path
said out loud. Then say in one line what kind of file it turned out to be, how many words came out,
how many were uncertain, and which of those were corrected. If the source was a folder, one text
file per original, sitting together in one directory.

When almost nothing comes out, do not guess. A PDF can be locked against copying, a photo can be
too dark to read, and a picture of a chart may genuinely have almost no words in it. Say which of
those it looks like, and what the next attempt would be.

## Others in this pack

- **make-it-readable**: once the words are out and someone has to read them, this restructures a
  draft so people finish it.
- **prove-it**: makes Claude show the receipt for work it says it finished, rather than taking the
  word for it.
- **grill-my-plan**: stress-tests a plan before any of it gets acted on.
- **remember-my-rules**: writes the CLAUDE.md that makes Claude remember these preferences next time.
- **first-build**: empty folder to one working thing, inside an hour.
- `tailor-my-resume` , read one job ad properly, interview them about the work behind their bullets, and rewrite the resume for that one job.
