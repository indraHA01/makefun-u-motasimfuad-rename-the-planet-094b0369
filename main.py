#!/usr/bin/env python3
"""Rename the Planet — make.fun entry.

Writes one funny new name for a planet in our solar system, plus the
why, in a single line to /output/entry.txt. Deterministic: the same
line every run, no network, no randomness, stdlib only.

The rename (123 characters, one line):
    Venus is now 'The Ex': hottest thing in the solar system, spins
    backwards, and rains acid on anyone who tries to come back.

Why this angle: the joke is an idea, not a pun on the planet's name.
Venus is the hottest planet in the solar system, it spins backwards
(retrograde rotation), and its clouds rain sulfuric acid — three traits
no other planet shares at once. An ex is hot, goes backwards, and turns
toxic the moment you come back: the why earns the name, and the name
would fit no other planet.

Run:  python3 main.py
"""

import os
import sys

# The entry, in two halves: the rename, then the why that earns it.
# Why the joke lands: Venus is the ex — hottest thing in the solar
# system, spins backwards, and rains acid on anyone who tries to come
# back. All three traits are real Venus facts, and together they fit no
# other planet, so the name is earned by the science, not just the pun.
ENTRY = (
    "Venus is now 'The Ex': hottest thing in the solar system, "
    "spins backwards, and rains acid on anyone who tries to come back."
)

# The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR lets the kit
# harness (or a local run) point the output somewhere else.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# House gate (RULES.txt): UTF-8 text, 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Fail loudly if the entry would fail the house gate."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"gate fail: {len(text)} chars, need 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("gate fail: entry is only whitespace")
    if "\n" in text:
        raise SystemExit("gate fail: entry must be one line")


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
