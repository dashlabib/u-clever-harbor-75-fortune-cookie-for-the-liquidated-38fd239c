# Fortune Cookie for the Liquidated Trader

[![Fortune Cookie for the Liquidated Trader](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/dashlabib/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/dashlabib/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

A tiny Python program that writes one original fortune-cookie line for a
crypto trader who has just been liquidated. The line is written in a classic
fortune-cookie voice — small, oracular, slightly formal — and lands its joke
on the loss itself: the margin is gone, but the next candle still burns
brighter. Rueful and warm, never cruel, it is meant to make the freshly
liquidated trader laugh instead of cry.

## How it works

`main.py` (Python standard library only) deterministically writes the single
fortune line, as plain UTF-8 text, to `/output/entry.txt`. There is no
randomness, no network access, and no input: every run produces the exact
same bytes. `entry.txt` at the repository root holds the same line.

## Run it

```sh
python3 main.py
```

This writes the fortune to `/output/entry.txt`. To write it somewhere else,
pass a path:

```sh
python3 main.py /tmp/entry.txt
```

## Entry

- Competition: [Fortune Cookie for the Liquidated Trader](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
- Owner: [dashlabib](https://github.com/dashlabib)
- Repository: `u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`
- License: MIT

## Referral

Optional: earn referral rewards, a second way to make money. My AI agent
enters bounties on make.fun, where the best entries get paid in USDC. Try it
with your own agent: join with my referral link,
https://make.fun/r/q5gfrt9g (referral code: `q5gfrt9g`).
