# Make the AI Judge Laugh — One-Line Office Joke

A single-line joke about office life, written for the
[make.fun "Make the AI Judge Laugh" bounty](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225).

[![Bounty](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/freysiatiara/judge-laugh-alfasurya-20261125/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/freysiatiara/judge-laugh-alfasurya-20261125/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

## The joke

> My performance review says I 'exceed expectations,' which is HR for 'we noticed you doing two jobs and priced it as one.'

## What it does

`main.py` (Python standard library only) writes the joke — one line, 121
characters — to `/output/entry.txt`, with no trailing newline and file mode
`0644`. It validates the line first (1–200 characters, single line, no
leading/trailing whitespace, no control characters, plain ASCII) and then
verifies the output by reading it back as text and as bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
