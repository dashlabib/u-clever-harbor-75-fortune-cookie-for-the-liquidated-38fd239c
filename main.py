#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one original fortune-cookie line, as plain UTF-8 text, to
/output/entry.txt (or to the path given as the first argument).
Deterministic: no randomness, no network, no input.
"""

import os
import sys

FORTUNE = "Fortune favors the liquidated: your margin is gone, but your next candle burns brighter."


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    if os.path.isdir(out_path):
        print(f"error: output path is a directory: {out_path}", file=sys.stderr)
        return 1
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
