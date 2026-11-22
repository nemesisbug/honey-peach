#!/usr/bin/env python3
"""Honey Peach — the picture that tastes of one ingredient.

Writes one image to /output/entry.png: a single honey-drizzled roasted
peach, caramelised and glistening, shot tight in warm golden light.
The picture is stored as a fixed asset (peach.png) next to this program;
this program copies it byte-for-byte, so every run produces identical
output: deterministic, no network, stdlib only.
"""

import hashlib
import os
import shutil
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peach.png")
OUTPUT = "/output/entry.png"


def main() -> int:
    with open(ASSET, "rb") as f:
        data = f.read()
    # Sanity: a whole PNG, 1024x1024, under the 1 MiB cap.
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "asset is not a PNG"
    assert len(data) <= 1_048_576, "asset exceeds 1 MiB"
    # Parse the IHDR chunk: width and height must be exactly 1024x1024.
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (1024, 1024), f"asset is {width}x{height}"
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "wb") as f:
        f.write(data)
    print(f"wrote {OUTPUT} ({len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
