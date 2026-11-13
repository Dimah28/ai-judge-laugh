#!/usr/bin/env python3
"""Make the AI judge laugh (make.fun bounty ai-joke-03).

Writes one joke to /output/entry.txt: a one-liner about AI coding agents.

The joke was built for the judge's own criteria, in order:
  1. On subject: it is about working beside an AI that writes code.
  2. Surprise: the punchline turns twice -- the agent blames the human,
     and then the human admits the agent was right.
  3. Truth: any developer who works beside an agent recognises the moment
     the agent points at the real cause and the cause is your own prompt.
  4. Economy: one line, no setup beyond what the punch needs, no
     explanation of itself.
  5. Freshness: a blame-reversal with a self-own kicker, not a stock
     "AI writes bugs faster" or "AI took my job" line.

Deterministic: the joke is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "My AI agent fixed the bug, then blamed me in a code comment \u2014 and it was right."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-280 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 280:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-280")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
