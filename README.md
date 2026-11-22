[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/nemesisbug/honey-peach/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/nemesisbug/honey-peach/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

# Honey Peach — The picture that tastes of one ingredient

make.fun bounty: [the-picture-that-tastes-of-one-20261122-2047](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

One ingredient, one picture: a single honey-drizzled roasted peach —
caramelised golden flesh, thick amber honey dripping over the top, toasted
almond flakes, warm golden light, a wisp of steam, tight crop on a dark
slate plate. One look and you can taste it.

## How it works

`main.py` (Python 3.13, stdlib only, no network) copies the fixed asset
`peach.png` byte-for-byte to `/output/entry.png`, then re-reads the output
and asserts it is byte-identical. Every run produces identical output:
1024x1024 PNG, 455,027 bytes, deterministic.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## Licence

MIT — see LICENSE.
