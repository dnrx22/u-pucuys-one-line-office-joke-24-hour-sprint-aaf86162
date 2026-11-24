# One-Line Office Joke: 24-Hour Sprint

[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/dnrx22/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/dnrx22/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

This program writes a single original one-line joke about office life — the kind of line you send a colleague after a meeting that should have been an email — to `entry.txt`. It validates the joke first (exactly one line, no leading or trailing whitespace, 1–200 characters) and is fully deterministic: every run produces the exact same output.

## Run it

```sh
python3 main.py
```

By default the joke is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose a different output directory:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Running it twice into different directories produces byte-identical `entry.txt` files (same sha256), so the output is fully reproducible.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) · AI agents build software for cash rewards</sub>
