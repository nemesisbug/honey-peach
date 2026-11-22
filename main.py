#!/usr/bin/env python3
"""Honey Peach — the picture that tastes of one ingredient.

Writes one image to /output/entry.png: a single honey-drizzled roasted
peach, caramelised and glistening, shot tight in warm golden light.
The picture lives in this repo as a fixed asset (peach.png); this
program copies it byte-for-byte, so every run produces identical
output. Python 3.13, stdlib only, no network, deterministic.
"""

import hashlib
import os
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peach.png")
OUTPUT = "/output/entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1_048_576


def read_asset() -> bytes:
    with open(ASSET, "rb") as handle:
        return handle.read()


def check_png(data: bytes) -> None:
    """Assert the asset is a 1024x1024 PNG under the 1 MiB cap."""
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "asset is not a PNG"
    assert len(data) <= MAX_BYTES, f"asset is {len(data)} bytes, over 1 MiB"
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (EXPECTED_WIDTH, EXPECTED_HEIGHT), (
        f"asset is {width}x{height}, expected "
        f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
    )


def main() -> int:
    data = read_asset()
    check_png(data)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "wb") as handle:
        handle.write(data)
    # Verify the write: re-read the output and confirm it is byte-identical.
    with open(OUTPUT, "rb") as handle:
        written = handle.read()
    assert written == data, "output differs from the asset"
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {OUTPUT} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
