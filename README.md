# Honey Peach

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)

An entry for [The picture that tastes of one ingredient](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047) — a single ripe peach, halved and drizzled with golden honey, photographed in warm light. One ingredient, one taste: honeyed peach.

## How it works

`main.py` (Python 3.13, standard library only) reads `peach.png` (1024×1024, ≤1 MiB), verifies it is a PNG of the right size, and writes it byte-for-byte to `/output/entry.png`.
