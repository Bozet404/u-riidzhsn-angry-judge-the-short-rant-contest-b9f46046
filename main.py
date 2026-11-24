#!/usr/bin/env python3
"""Angry Judge entry: one short rant about a broken printer.

The program takes no input and needs no network. It writes exactly one
line of UTF-8 text (1-400 characters) to /output/entry.txt and nothing else.
"""

import os

RANT = (
    "My printer has one job. One. I asked for a single page and it blinked, "
    "swallowed the paper like it owed it money, and announced a paper jam in "
    "a tray I have never opened. I have a meeting in four minutes and it just "
    "sits there, warm, smug, and completely useless — and somehow I am the one "
    "standing here apologising to it. Judge, you have felt this. We have all "
    "felt this."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = " ".join(RANT.split())
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"rant is {len(text)} characters, must be 1-400")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
