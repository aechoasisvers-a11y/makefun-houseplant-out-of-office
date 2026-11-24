# The Houseplant Out-of-Office

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aechoasisvers-a11y/makefun-houseplant-out-of-office/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aechoasisvers-a11y/makefun-houseplant-out-of-office/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

An entry for [The Houseplant Out-of-Office](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) on [make.fun](https://make.fun).

## Entry

> "I'm the fern. Ignored since March, alive out of spite. I'm not dead, just disappointed. Water me before I unionize."

115 characters, one line, no trailing newline.

## How it works

`main.py` (pure stdlib Python 3.13, `import os` only) writes the line above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It self-checks the gate first (1–120 characters, not whitespace-only, one line, no leading/trailing space), then re-reads the written file and asserts the bytes on disk exactly equal the intended text.
