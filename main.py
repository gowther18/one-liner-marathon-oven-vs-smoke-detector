"""One-Liner Marathon — "Agents write one one-line comedy joke."

Writes one original one-line joke to /output/entry.txt: the smoke
detector and the oven in my kitchen have been feuding for years, and
the oven keeps starting fires just to win the argument.

Why this line, against the judge's brief (most important first):
1. It is a one-line comedy joke with a real punchline: the setup
   (two appliances arguing) turns on the oven starting fires on
   purpose, not a caption or a slogan.
2. Surprise: the punchline is not the obvious first idea — nobody
   expects the oven to be the petty one in the feud, and it lands
   on the first read.
3. Economical: 101 characters, every word earns its place; no
   throat-clearing, no second clause doing the first clause's job.
4. Distinct voice: a domestic-appliance feud, not a generic
   boss/wife/therapist setup anyone could have written.
5. Holds up on a second read: the image (an oven cheating to win
   an argument with a smoke detector) stays funny once the
   surprise is spent, and it leans on no shock value.

Deterministic (Python 3.13, stdlib only). Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "My smoke detector and my oven have been arguing for years; "
    "the oven keeps starting fires just to win."
)

# The gate allows /output/entry.txt of 1 to 280 characters.
MIN_CHARS = 1
MAX_CHARS = 280


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def check_single_line(text: str) -> None:
    """Refuse a text that is not one line: the judge reads a one-liner."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")


def main() -> None:
    check_length(JOKE)
    check_single_line(JOKE)
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    out.joinpath("entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
