---
name: remember-my-rules
description: Interview the user about how they work, then write their project's CLAUDE.md so Claude remembers their preferences in every future session instead of being told again each time. Use this the moment someone says Claude keeps forgetting, keeps doing it the wrong way, keeps using the wrong format, or asks "how do I make it remember", "where do I put my preferences", "can I train it on my style", "set up CLAUDE.md", "why do I have to repeat myself". Also use it when someone has been correcting the same thing 3 or 4 times in a session, even if they have not asked for anything, because that is exactly what a rules file exists to stop. Not for cleaning up a CLAUDE.md that already exists and has grown too long, and not for teaching Claude a whole multi-step workflow, which is its own skill rather than a rule.
---

# House Rules

## What this is for

Claude starts every session knowing nothing about how you like to work. You correct it, it adapts for an hour, the session ends, and the next one begins exactly where the first did. People assume this is a memory problem and that nothing can be done about it. It is a file problem, and it takes 15 minutes to fix once.

A file called `CLAUDE.md`, sitting in the folder you work in, is read at the start of every session in that folder. Whatever is in it, Claude knows before you type anything. That is the whole mechanism. The hard part is not creating the file. The hard part is knowing what belongs in it, and almost nobody gets that right from a blank page, which is why this skill interviews rather than hands over a template.

## What belongs in it, and what does not

This is the distinction the whole skill turns on, so it comes first.

A rules file holds things that are **stable and yours**: how you want things written, what you never want done, which tool you use for a job, the names of things in your work, the standard a piece of work has to reach before you would call it finished. These stay true next month.

It does not hold **what is happening right now**: what you are working on this week, the status of a task, a list of files, a log of what changed. That information goes stale within days, and a stale rules file is worse than no rules file, because Claude will follow it confidently.

The test to apply to any candidate line: will this still be true in 3 months? If no, it belongs in a note, a task list, or nowhere.

## How to run the interview

Ask one question at a time and follow what they actually say. A form gets you a form's answers. The goal is to leave with 10 to 20 lines that are genuinely theirs, which is a different thing from filling in every section below.

**Start from the friction, not from the categories.** The best opening is some version of: *what has Claude done in the last week that made you sigh?* People cannot answer "what are your preferences" from cold, but they can always answer that one, and the answer is a rule.

Then follow these threads, in whatever order the conversation goes:

1. **Corrections they have made more than once.** If they corrected the same thing 3 times, it is a rule and they have already written it, out loud. Read it back in their own words.
2. **How they want things written.** Not "professional" or "friendly", which mean nothing on their own. Ask for a piece of writing they liked and one they did not, and find the actual difference. Words they never want used. Length. Whether they want the answer first or the reasoning first.
3. **The tools and names in their work.** Which spreadsheet program, which editor, what they call their own projects, folders or clients. Claude guessing a name wrong is a small error that costs a correction every single time.
4. **What they never want done without being asked.** Deleting anything. Sending anything. Changing a file they did not name. Installing something. This is the section people are most grateful for later, and they rarely raise it themselves, so raise it.
5. **What "finished" means to them.** The check a piece of work has to pass before Claude says it is done. This one line prevents more disappointment than the rest of the file combined.

**Press once on anything vague.** "Make it shorter" is not a rule; "under 200 words unless I ask for more" is. "Do not be too formal" is not a rule; "never open with Certainly or Great question" is. Press once, take the answer, and move on. Twice is an interrogation and they will start making things up to end it.

**Never invent a preference to fill a gap.** An invented rule is followed just as faithfully as a real one, and the user will not know why the output went strange. Where a section is thin, leave it out and say so.

## Writing the file

Keep it short. A rules file that is 40 lines long gets read and followed. One that runs to 300 lines gets skimmed, and lines deep inside it stop reaching Claude's hands. If the interview produced more than fits comfortably, keep the rules that prevent the most repeated corrections and let the rest go.

Write each rule so it says what to do rather than what to avoid, where that is possible, because a rule phrased only as a prohibition leaves the alternative unstated. "Answer first, then the reasoning" beats "do not bury the answer".

Carry their phrasing across where it is vivid. A rule in their own words is one they recognise later and can edit with confidence.

Group into headings only when there are enough lines to need them. Four rules under three headings is theatre.

The template and a worked example are in `references/template.md`. Read it before writing, and treat it as a shape rather than a form to complete.

## After you write it

Show them the whole file and read the rules back in plain language. This is the moment they catch the one you got backwards, and it is much cheaper to catch it here than in three weeks when they cannot remember why everything is coming out wrong.

Then tell them two things they will otherwise learn the hard way:

- **Where it lives decides where it applies.** In a project folder it governs that project. In their home folder under `.claude/`, it governs everything they do.
- **It is meant to be edited.** The next time they correct Claude twice on the same thing, that correction is a new line in this file. A rules file that never changes after the day it was written is a file that stopped being true.

## Others in this pack

- `first-build`, take them from an empty folder to one working thing. Run `remember-my-rules` after, once they know what they actually want it to stop doing.
- `prove-it`, when Claude says it is done, make it show the receipt.
- `grill-my-plan`, before they commit to an approach, find where it breaks.
- `extract-text`, pull the words out of a screenshot, a photo or a scanned PDF.
- `make-it-readable`, restructure a draft so people finish reading it.
- `tailor-my-resume` , read one job ad properly, interview them about the work behind their bullets, and rewrite the resume for that one job.
