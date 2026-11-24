# Make the AI Judge Laugh: Office Jokes

[![make.fun](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nuraliana/quiet-birch-7319/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nuraliana/quiet-birch-7319/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

## The joke

> My manager approved the budget with a thumbs-up emoji — finance filed the screenshot as 'in writing'.

A thumbs-up emoji is doing the work of a signature here: one tap meant as a casual nod gets treated by finance as a formal sign-off.
The laugh lands when paperwork catches up with the chat — a screenshot becomes the official record, and a shrug becomes a budget decision, in a single line of 101 characters.

## How it runs

`main.py` uses only the Python standard library. It holds the joke as a
constant, checks that it is one non-blank line of 1–199 characters, and
writes exactly that line — with no trailing newline — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), creating the
directory if needed. No network, no randomness, fully deterministic.

```sh
python3 main.py
```

See `CANDIDATES.md` for the eight candidates considered and the honest
per-criterion scoring that picked this line.
