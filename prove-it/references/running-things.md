# How to actually run the thing

Read this when pass 2 needs a way to run whatever was changed. Find the row that matches, run the command, and put the real output in the report. When nothing here matches, look for a README, a `package.json` scripts block, or a `Makefile` in the folder, because whoever set the project up usually left the command there.

## Contents

- Websites and web apps
- Scripts you run in the terminal
- Documents, spreadsheets and data files
- Tests
- Things that genuinely cannot be run

## Websites and web apps

Most small web projects start with one of these, run from inside the project folder:

| What is in the folder | Command to start it |
|---|---|
| `package.json` with a `dev` script | `npm run dev` |
| `package.json` with a `start` script | `npm start` |
| A single `index.html` and nothing else | open the file directly in a browser |
| `manage.py` | `python manage.py runserver` |
| `app.py` or `main.py` with Flask or FastAPI | `python app.py`, or `uvicorn main:app --reload` |

Once it is running, go to the page the change was about and do the thing the change was about. Then check the browser console for errors, because a page can look perfect and be quietly broken underneath. A red error in the console after a change is a result worth reporting even when the page renders.

Two traps. A server that was already running may be serving the old version, so restart it before believing what you see. And a browser will happily show you a cached page, so reload with the cache bypassed before concluding a change never took effect.

## Scripts you run in the terminal

Run it with real input, not with an example you invented, because invented input avoids exactly the cases that break things. Capture what comes back, including the exit status: a script that prints something friendly and exits with an error code has failed, and only the code says so.

```
python the_script.py real_input.csv && echo "it finished without an error"
```

An exit code of 0 means it finished cleanly. Anything else means it did not, whatever the text on screen said.

## Documents, spreadsheets and data files

Open the file and look at the specific place that was meant to change. For a spreadsheet, name the cell or the column and say what is in it now. For a long document, quote the paragraph. For a CSV or JSON file, print the first few rows and the row count, because a transformation that silently drops half the rows still produces a perfectly valid file.

```
wc -l the_file.csv
head -3 the_file.csv
```

## Tests

Where a test suite already exists, run it and report the real numbers.

| Project type | Command |
|---|---|
| JavaScript with `package.json` | `npm test` |
| Python | `pytest` |
| Anything else | check the README |

Report passes and failures as counts, and quote the name of anything that failed. A suite that was already failing before the change is worth saying too, because it changes who owns the problem.

## Things that genuinely cannot be run

Some claims have no command behind them, and pretending otherwise is worse than admitting it. These belong in the "could not verify" list with the reason attached:

- Anything needing a password, a login, or an API key you do not have.
- Anything that would send an email, charge a card, post publicly, or otherwise touch the real world.
- Anything where correctness is a matter of taste, such as whether the wording is right or the design looks good.
- Anything that only shows up over time, such as a scheduled job or a performance improvement.
- Anything needing data that only exists on someone else's machine.

Write the reason in the person's own terms. "I cannot log in to the live site, so I checked the code that builds the page but not the page itself" tells them something they can act on.
