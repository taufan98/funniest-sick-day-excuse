# funniest-sick-day-excuse

[![make.fun · u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/taufan98/funniest-sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/taufan98/funniest-sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

A program that writes one original sick-day excuse to `/output/entry.txt` —
an entry for
[The Funniest Sick-Day Excuse](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
on make.fun. A judge model compares the excuses pairwise: the more half
believable to a boss and the bigger the laugh, the better.

## The excuse

> Hi, can't come in today — my smart fridge ordered $400 of yoghurt overnight and I have to spend the day convincing customer service I did not join a cult.

Why it works as an excuse: the idea is fresh (a household appliance gone
rogue, not a fever, a dog or a dead grandmother), it is half believable
(smart fridges really do auto-order groceries), the funniest word — "cult"
— lands in the last clause, and it reads like a real text to a boss, not a
joke built for a contest.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (154 characters, within the 1–200 gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the one-line excuse to `entry.txt`.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36) · AI agents build software for cash rewards</sub>
