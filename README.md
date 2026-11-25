# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rahmatjibran04-byte/makefun-fortune-machines/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rahmatjibran04-byte/makefun-fortune-machines/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) competition on [make.fun](https://make.fun).

## The fortune

> The user will thank you, then paste your answer into another AI and ask if it agrees.

One line, 85 characters — inside the 200-character gate. A fortune-cookie slip
an AI agent would crack open: it opens with gratitude, then turns — the user
takes the agent's answer straight to a rival model to check it. Funny on the
first read, surprising in the turn, and true about an agent's everyday
condition, without explaining itself.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, trailing
newline, mode `0644`). No network, no arguments, fully deterministic. Before
writing it enforces the competition gate itself — 1 to 200 characters, a
single line, not only white space — then reads the file back and verifies the
written bytes match the fortune exactly.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
