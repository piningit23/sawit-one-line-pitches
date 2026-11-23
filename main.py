#!/usr/bin/env python3
"""One-line pitch for make.fun's 'A Day of One-Line Pitches' bounty.

Writes a single sentence (197 characters) to entry.txt. The sentence
invites a friend who has never coded to describe their app idea in
plain words and let make.fun's AI agent build it by tonight.
"""

import os
from pathlib import Path

PITCH = (
    "Tell make.fun's AI agent your app idea in plain words, and by "
    "tonight you'll have a real working app to show your friends "
    "\u2014 no code, no cost to enter, just the idea you've always "
    "had finally built."
)


def validate(text: str) -> str:
    """Keep the gate simple: 1-240 chars, non-blank. No period-count
    guard — "make.fun" itself contains a period, so counting periods
    would wrongly reject a valid one-sentence pitch."""
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"pitch must be 1-240 chars, got {len(text)}")
    return text


def main() -> None:
    text = validate(PITCH)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
