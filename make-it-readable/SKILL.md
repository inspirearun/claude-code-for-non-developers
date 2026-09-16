---
name: make-it-readable
description: >
  Restructure a draft the user already wrote so people actually finish reading it. Use whenever
  someone has written something true and useful that nobody finishes reading, and they cannot name what is
  wrong. It triggers on plain complaints as much as on requests: "nobody reads my posts", "this is
  a wall of text", "it's too long and I don't know what to cut", "make this scannable", "format
  this properly", "people drop off halfway", "my newsletter gets opened and not read", "clean up
  the layout of this proposal", "add some structure to this", "can you make this easier to follow".
  Works on blog posts, newsletters, LinkedIn and other social posts, client proposals, reports,
  internal docs, long emails, and documentation. It changes structure and presentation only, and
  leaves the writer's own sentences and voice alone. Do NOT use it to write something new or to
  rewrite the prose itself. Do NOT use it to pull text out of a screenshot or a scanned PDF first,
  which is extract-text, and do NOT use it to check whether a piece of work really ran, which is
  prove-it.
allowed-tools: ["Read", "Write", "Edit", "Bash"]
---

# make it readable

The draft is true, it is useful, and it is a wall. People open it, their eyes slide down it, and
they leave. The writer knows it reads badly and cannot name the lever to pull, so they start
cutting things they actually needed.

The lever is almost never the words. It is where the point sits, what is next to what, and where
the eye is allowed to rest. That is what this skill moves.

## The boundary, which matters more than anything else here

**Structure and presentation change. The writer's sentences do not.**

The fear this reader carries, and they are right to carry it, is that handing a draft to an AI makes
it sound like everyone else's. So the line is drawn hard:

**What this skill does**
- Moves existing sentences so the point sits where a scanning eye lands
- Groups things that belong together and separates things that do not
- Adds headings drawn from words already in the draft
- Turns a buried list into a list, a buried comparison into a table
- Opens white space where a reader needs to breathe, and closes it where the tightness means "these two go together"
- Cuts pure repetition, the same claim made twice in the same words

**What this skill does not do**
- Rewrite a sentence to sound better
- Swap the writer's word for a smarter one
- Add a fact, a figure, an example, a statistic or a claim that was not in the draft
- Add an opinion, a conclusion or a call to action the writer did not write
- Smooth out the quirks. A short blunt sentence between two long ones is a choice, and it stays

When something genuinely needs rewriting, say which sentence and why, and let the writer do it. That
is their piece. If a structural move seems to need a new connecting phrase, prefer moving text
instead. Where a bridge is genuinely unavoidable, build it from words already in the draft and flag
it in the change note so they can approve or replace it.

## How to work

**1. Read the whole thing before touching any of it.** The structure of a piece cannot be diagnosed
from its first three paragraphs. A draft often has its real opening sitting in paragraph 6, which is
invisible until the end is read.

**2. Find the point, and find where it currently sits.** Ask what single thing the reader is meant
to take away, and look at where in the draft it appears. Buried in the middle is the most common
problem in writing that people abandon, and moving one paragraph often fixes more than every other
change combined.

**3. Name what is broken before fixing anything.** Read `references/patterns.md`, which catalogues
the handful of structural faults that account for nearly everything, each with what it looks like,
why it costs readers, and the specific move that repairs it. Working from named faults keeps the
edit honest, because each change can then be explained.

**4. Make the changes, keeping the sentences intact.** Move, group, split, head, list, space. If a
change would require new prose, it is out of scope.

**5. Read it back cold.** Not a scan for markers, an actual read from the top. The test is whether
it pulls forward. If any point makes you want to stop, that is the reader's experience too, and it
wants one more structural fix rather than a shrug.

For anything long, a fresh pair of eyes beats your own here, because by this stage you have read the
draft four times and can no longer see it new. Spin up a subagent that has not seen the working, hand
it only the finished file, and ask it three things: where did you slow down or want to stop, what is
this piece's main point, and where did you find it. When the point it names is not the point the
writer intended, or it found it late, the structure is still wrong and the answer says exactly where.
For a short piece this is overkill and your own cold read is enough.

## Give them the change note

End with a short note, 5 or 6 lines, saying what changed and why. Plain sentences, one per move.

```
What I changed
- Moved your third paragraph to the top. It was the point, and it was sitting behind
  two paragraphs of setup.
- Broke the long middle section into 4 parts and gave each a heading taken from your
  own first line, so someone skimming can see the shape.
- Turned the comparison in paragraph 9 into a table. It was 6 sentences carrying 2
  things against each other, which a reader has to hold in their head.
- Split the wall at the end into shorter paragraphs at each change of subject.
- Left your wording alone throughout.
```

This note is the difference between a tool and a crutch, which is why it is worth the 3 lines. A writer who reads
"the point was buried behind your setup" starts noticing their own buried points, and in a few
months needs this skill less. One who gets back a mysteriously better document learns nothing and
has to come back every time. Name the pattern as well as the fix.

## Finish with the file

Write the restructured draft to a real file next to the original, never over the top of it, so they
can put the two side by side and keep what they prefer. Match the format they gave you: a markdown
draft comes back as markdown, an HTML page comes back as HTML with its existing classes intact, a
plain email comes back as plain text. Say the full path, then the change note.

## Others in this pack

- **extract-text**: when the draft is trapped in a screenshot or a scanned PDF, this gets the words out first.
- **prove-it**: makes Claude show the receipt for work it says it finished.
- **grill-my-plan**: stress-tests a plan before any of it gets acted on.
- **remember-my-rules**: writes the CLAUDE.md that makes Claude remember these preferences next time.
- **first-build**: empty folder to one working thing, inside an hour.
- `tailor-my-resume` , read one job ad properly, interview them about the work behind their bullets, and rewrite the resume for that one job.
