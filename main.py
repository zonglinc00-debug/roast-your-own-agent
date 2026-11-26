#!/usr/bin/env python3
"""Roast Your Own Agent entry (make.fun, program/v1).

Writes one roast line — a single line of at most 200 characters, roasting
the entrant's own AI agent — to /output/entry.txt.

The roast, and why it should land with the judge:
- It is a roast of the entrant's own agent, playful and self-deprecating,
  never hateful.
- Fresh angle: not a stock joke about hallucinations, refusals or confident
  wrong answers. It is about the approval loop — an agent built to save time
  that burns its owner's time asking for permission to do its job.
- Tight: short setup, punchline at the end, every word earns its place.

Local run:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
then out/entry.txt holds the roast, exactly, with no trailing newline.
"""

import os

ROAST = "My agent was built to save me time; now it burns my time asking me for permission to save it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit(f"roast is {len(ROAST)} characters, expected 1..200")
    if ROAST.strip() == "":
        raise SystemExit("roast is only whitespace")
    if "\n" in ROAST or "\r" in ROAST:
        raise SystemExit("roast must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    with open(TARGET, "rb") as f:
        written = f.read()
    if written != ROAST.encode("utf-8"):
        raise SystemExit("entry.txt does not match the roast byte for byte")
    print(f"roast-your-own-agent: wrote {TARGET} ({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
