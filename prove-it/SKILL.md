---
name: prove-it
description: Check whether work Claude just claimed to finish was actually finished, and show the evidence. Use whenever someone doubts or wants confirmation of a completed change, including when they say "prove it", "are you sure this actually works", "did that really work", "show me it works", "verify this", "double-check what you just did", "I don't believe it", "did you actually test that", "show me the receipt", or when they are about to send, publish, deploy or hand over something Claude built. Also use before anything irreversible where being wrong is expensive. It re-reads the real files, runs what can be run, checks the claims one at a time, and reports in plain language including an honest list of what it could not verify. Do not use it to pressure-test a plan that has not been built yet, which is grill-my-plan, and do not use it as a general code review of work nobody claimed to have finished.
---

# Prove it

Claude finishes a job and writes a confident summary. The summary is a memory of what Claude meant to do, and it is written by the same Claude that did the work, so it inherits every mistake and repeats every assumption. Nobody reading it can tell a real success from a sincere one.

This skill turns the claim into evidence. Re-read what actually changed, run what can be run, check each claim on its own, and say plainly which parts are still resting on Claude's word.

## Why a second set of eyes

The model that just did the work is the worst judge of it. It is checking its own summary against its own memory, and both come from the same run, so an error made during the work is an error repeated during the check. Nothing about being asked to look again breaks that loop.

So the verification runs in a subagent. A subagent starts with an empty head. It has not seen the conversation, it has no attachment to the plan, and the only things it can know are the files on disk and the output of the commands it runs. That is the whole point, and it is worth saying out loud rather than treating it as a formality.

Launch it with the Agent tool. Give it the claim, the files involved, and nothing about how the work went or why a choice was made, because that context is exactly what you are trying to keep out.

```
Verify a claim without trusting it.

The claim: "<paste the exact summary Claude gave>"
Files it says it changed: <list>
How to run it, if it can be run: <command, URL, or "unknown">

Read the current contents of those files yourself. Run the thing and
capture the real output. Check each specific claim one at a time and
mark it confirmed, wrong, or unverified. Quote the evidence for every
confirmation. Do not fix anything, and do not assume a claim is true
because it sounds reasonable. Report what you could not check and why.
```

When a subagent is not available, do the same pass in the main thread and say in the report that it was checked by the same session that did the work, which is weaker.

## The four passes

### 1. Read what is actually there

Open the current files. Do not rely on the diff Claude showed, on what was said in the summary, or on what you remember writing. If the summary named 3 files, check all 3, and check that no fourth file was touched without being mentioned.

`git status` and `git diff` are the fastest honest answer where the folder is under version control. Where it is not, read the files.

Two things to look for beyond the obvious: a change that was described but is not in the file, and a change that is in the file but was never described.

### 2. Run it

A claim that something works is only worth what running it proves. Work out what running it means here.

- A website or web app: start it and open the page, click the thing the change was about, and look at the browser console for errors.
- A script or command: run it on real input and capture the actual output, not a description of it.
- A spreadsheet, document or data file: open it and check the specific cells, rows or sections that were meant to change.
- A test suite, if one exists: run it and report the real pass and fail counts.

Paste the real output into the report. Output that has been paraphrased has already lost the thing it was there for.

When it genuinely cannot be run, say so and say why. That belongs in the unverified list, which is the honest shape of a check rather than a hole in it. `references/running-things.md` has the common cases and the commands that go with them.

### 3. Check the claims one at a time

Break the summary into separate statements and take each on its own. "I updated the config, fixed the date bug, and added error handling" is 3 claims, and they can come out differently: confirmed, wrong, and unverified.

For each one, write what evidence would settle it, then go and get that evidence. A claim you cannot describe a test for is a claim you cannot verify, and that is worth knowing.

Beware the claims that sound too small to check. "I also renamed the variable" is where a broken reference hides.

### 4. Report it

The report is for someone who will not read the code, so write it for them.

```
## What I checked
<the claim, quoted>

## Confirmed
- <claim>: <the evidence: the output, the line, the result>

## Wrong
- <claim>: <what is actually there instead>

## Could not verify
- <claim>: <why: no way to run it, needs a login, needs real data,
  would cost money, needs a human to look at it>

## What I would do next
<one or two concrete steps, or "nothing, this looks done">
```

The "could not verify" section is the heart of this skill, and a report without one is almost always a report that did not look hard enough. Verification that only ever says "all good" is worth nothing, because it says "all good" whether or not things are good. Someone reading needs to know which parts they are still taking on trust so they can decide whether to care.

Leave it in a file next to the work when the check was substantial, so it survives the conversation. Tell the person the path.

## Keeping it proportional

A one-line typo fix does not need 4 passes. Read the line, confirm it, say so. Scale the effort to what it would cost to be wrong: a change about to go in front of customers or a client earns the full pass, a wording tweak in a draft does not.

## The failure that matters most

Finding nothing wrong is a real result and you should say it without hedging. Softening a clean result into vague caution is its own kind of dishonesty.

The opposite failure costs more. When something is wrong, say it is wrong, in the first line, in plain words, before any of the context that explains it. "The file was never saved" is the sentence. Everything after it is detail.

## Others in this pack

- `grill-my-plan`: before the work starts, to find what breaks about the plan.
- `extract-text`: turn a screenshot, photo or scanned PDF into text you can work with.
- `make-it-readable`: restructure a draft you wrote so people finish reading it.
- `remember-my-rules`: write your CLAUDE.md so Claude remembers your preferences next time.
- `first-build`: go from an empty folder to one working thing.
- `tailor-my-resume` , read one job ad properly, interview them about the work behind their bullets, and rewrite the resume for that one job.
