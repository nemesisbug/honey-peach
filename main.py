#!/usr/bin/env python3
"""Honey Peach — the picture that tastes of one ingredient.

Reads peach.png (1024x1024, <=1 MiB) from the repository root and writes it
byte-for-byte to /output/entry.png.
"""
import hashlib
import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "peach.png")
DST = "/output/entry.png"
MAX_BYTES = 1 << 20  # 1 MiB


def read_png_header(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("peach.png is not a PNG file")
    if len(data) < 24:
        raise SystemExit("peach.png is too short to be a PNG file")
    width, height = struct.unpack(">II", data[16:24])
    return data, width, height


def main():
    data, width, height = read_png_header(SRC)
    if (width, height) != (1024, 1024):
        raise SystemExit(f"peach.png is {width}x{height}, expected 1024x1024")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"peach.png is {len(data)} bytes, over the 1 MiB limit")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    # Verify-after-write: re-read the output and assert it is byte-identical.
    with open(DST, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("verification failed: /output/entry.png differs from peach.png")
    print(f"wrote {DST}: {len(data)} bytes, 1024x1024, "
          f"sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
