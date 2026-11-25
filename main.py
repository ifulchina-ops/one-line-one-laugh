#!/usr/bin/env python3
"""One Line, One Laugh (make.fun u-coral-404-one-line-one-laugh-22f2c9f3).

The entry is a single funny line, written to /output/entry.txt.
The line is a constant in this file, so two runs always produce
identical bytes. No network, no randomness, no input files: the
line is the whole entry, exactly as the brief asks.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = (
    "My Roomba left me a note: 'I found dust under the couch you "
    "swore you cleaned. We're done. The cat gets custody.'"
)

_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.txt")


def main() -> None:
    # Competition limits: one line, at most 200 characters, not only
    # whitespace. Validate the constant before writing anything.
    if not LINE.strip():
        raise SystemExit("line is empty or only whitespace")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")
    if len(LINE) > 200:
        raise SystemExit(f"line is {len(LINE)} characters, over the 200 limit")
    os.makedirs(_OUT_DIR, exist_ok=True)
    with open(_DST, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
