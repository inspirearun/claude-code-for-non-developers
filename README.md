# The First Seven

Claude Code, for people who were told it was not for them.

Seven skills covering the first week.

If you have just installed Claude Code and everyone has told you it is for developers, this pack is the argument against that. Each of the seven does one job you already have, and between them they cover the first week: getting started, getting it to remember how you work, getting the words out of things, making what you write readable, fixing the resume that is not getting callbacks, and checking that any of it is actually true.

## What each one does

| | You say | You end up with |
|---|---|---|
| **Something You Built**<br><code>first-build</code> | "I don't know where to start" | One small working project, picked from a job you already do by hand, finished inside an hour |
| **Claude That Knows You**<br><code>remember-my-rules</code> | "it keeps forgetting how I like things" | A CLAUDE.md that records how you want Claude to work, read at the start of every future session |
| **What It Actually Did**<br><code>prove-it</code> | "are you sure that actually worked?" | A plain-language report of every claim it checked, and an honest list of what it could not |
| **Your Plan's Weak Points**<br><code>grill-my-plan</code> | "poke holes in this before I start" | The assumption everything rests on, the cost you had not counted, and the case where it fails |
| **Words Out Of Pictures**<br><code>extract-text</code> | "get the text out of this screenshot" | The text from screenshots, photos, scans and PDFs, with anything uncertain marked rather than guessed |
| **Your Voice, Easier To Read**<br><code>make-it-readable</code> | "nobody reads my posts" | A clearer draft that still uses your own sentences |
| **A Resume For This Job**<br><code>tailor-my-resume</code> | "my resume isn't getting callbacks" | An honest resume rewritten for one specific job ad, with a note on the gaps to prepare for |

The name in bold is what the skill gets you. The name underneath is what you type.

## Installing

Copy the folders into your skills directory:

```
~/.claude/skills/
```

Restart Claude Code. Type `/` and you will see them listed. You can also just describe your problem in your own words. Each skill knows the phrases people actually use, so you rarely need to name it.

`extract-text` is the only one that needs anything installed beyond Claude Code. Ask it to check, and it will tell you what is missing and the one command that gets it.

## The order that works

Most people get the most out of these in this order, and the reason is worth knowing.

1. **first-build**, because nothing else matters until one thing of yours is running.
2. **remember-my-rules**, straight after, because an hour of building is what teaches you what you actually want Claude to stop doing. Run the interview cold and you will invent preferences you do not have.
3. The other four as the need arrives.

## What these are

A skill is a folder with instructions in it. Claude reads the instructions when the moment fits, and then behaves that way without being told again. That is the entire idea, and it is why these are readable files rather than software. Open any of them and change a line, and the skill changes.

That is also the invitation. The last thing this pack teaches is that you can write your own.
