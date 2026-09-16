---
name: first-build
description: Take someone who does not write code from an empty folder to one small thing that actually works and that they can show another person, inside an hour. Use it for a first build, a first project, a first app, or whenever someone says "I don't know where to start", "what should I build first", "I installed Claude Code, now what", "can I build something without coding", "help me make a tool for my work", or describes a job they do by hand every week and wonders if it could be automated. Also use it when a beginner has picked something far too large for a first attempt, because rescoping is most of the job. Not for adding to a project that already runs, and not for teaching Claude their preferences, which is remember-my-rules.
---

# First Build

## What this is for

Most people's first attempt at building something with Claude Code fails for one of two reasons, and neither is technical. They pick something too big, so nothing works for days and they stop. Or they pick something with no visible result, so even when it works they cannot tell, and it never feels real.

The job here is to get one person to the moment where a thing they described in their own words is running in front of them. Everything else follows from that moment, and almost nothing follows without it.

So the bar is deliberately low and deliberately strict: **one thing, working, visible, inside an hour, that they would show somebody.**

## Choosing what to build

This is where the hour is won or lost, so spend real time here and do not let them rush past it.

**Start from a job they already do by hand.** Ask what they did last week that was boring and repetitive. Renaming files, copying numbers between sheets, checking whether a list of links still work, reformatting a client's messy export, pulling the same 5 figures into the same report. The answer is almost always a good first project, and it has a property that matters more than anything else: they will know instantly whether the result is right, because they have done it by hand.

**Judge every candidate against 4 things:**

1. **The result is visible.** A file appears, a page opens, a number prints. Something changed that they can see without being told.
2. **They can tell whether it is correct** without trusting anyone.
3. **It needs no account, no key, no payment.** The day someone hits a signup wall on their first build is the day they stop. Anything touching a paid service or a login waits for the second build.
4. **One sentence describes it.** If describing it needs "and then", it is two projects. Take the first half.

**Say no out loud when the idea is too big.** People arrive wanting an app with users and logins. Do not quietly build something smaller and hope they do not notice. Tell them the big thing is a real project and this is not that, name the smallest piece of it that satisfies the 4 tests, and build that piece today. The full version is a much easier conversation once something of theirs is running.

Worked examples of good and bad first projects, and how the bad ones were cut down, are in `references/project-picker.md`.

## Running the build

**Set the folder up first, and say what you are doing.** A new folder with a plain name, in a place they will find again. Tell them where it is and why it exists. A beginner who cannot find their own project later has lost it.

**Build the smallest version that runs, then run it in front of them.** Not the version with options and error handling. The version that does the one thing, once, on their real data. Run it and show the output. This is the moment the whole hour is for, and it should arrive well inside the first 20 minutes.

**Use their real files from the start, not made-up examples.** Sample data lets a bug hide, and worse, it keeps the project feeling like a lesson instead of their work.

**Narrate in their language, not in the tool's.** Say what is happening and why, in words they already have. They do not need to know what a dependency is to understand "this needs one extra program, here is how we get it, this is what it does". Explaining a term in the same breath you use it is fine and builds their vocabulary. Using it and moving on is not.

**When something breaks, and it will, treat it as part of the plan.** Say plainly what went wrong and what you are about to try. This is the single most important thing a beginner learns in the first hour, because their belief is that errors mean they did something wrong and are not cut out for this. Watching an error get read and fixed calmly, twice, changes what they believe they are capable of more than a clean run ever would.

**Stop when it works.** The temptation once it runs is to make it better. Resist it, and say why: they should leave with a working thing and their own list of what to add next, because that list is what brings them back tomorrow.

## Finishing

Three things before you are done, and none takes long.

1. **Show them how to run it again themselves.** Written down, in the folder, in plain words. A project they cannot start without you is a demonstration, not a tool.
2. **Write a short README in the folder**: what this does, how to run it, what to change if their situation changes. Write it for them in 6 months, who will have forgotten everything.
3. **Ask what they would add next** and write the list into the README without building any of it. That list is theirs, and the second build starts from it.

Then say the honest thing: they described a job in their own words and now a machine does it. That is what the whole of this is, and nothing that comes later is different in kind, only in size.

## Others in this pack

- `remember-my-rules`, run this next. After an hour of building they know exactly what they want Claude to stop doing, and that is when the interview produces real answers.
- `prove-it`, when Claude says a change is done, make it show the receipt.
- `grill-my-plan`, before committing to a bigger build, find where it breaks.
- `extract-text`, pull the words out of a screenshot, a photo or a scanned PDF.
- `make-it-readable`, restructure a draft so people finish reading it.
- `tailor-my-resume` , read one job ad properly, interview them about the work behind their bullets, and rewrite the resume for that one job.
