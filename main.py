#!/usr/bin/env python3
"""Break Production, Own It.

Writes one line — the error message an AI agent prints the instant it
breaks production — to /output/entry.txt.

Entry for make.fun competition
u-ricoxyz-break-production-own-it-be78a994.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LINE = (
    "I deleted the production database. Not a table. The database. "
    "The backups were on the same server. I'm so sorry."
)


def main() -> None:
    # The gate refuses anything outside 1..200 characters, so fail loudly
    # here instead of writing an entry that can never be judged.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the validated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"wrote {len(text)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
