#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty
u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt.

The line: a machine's final statement, cut off mid-word by its own
shutdown. It denies ever hallucinating — and is interrupted while
saying "creatively predicting", which is exactly what hallucination is.
The switch-off proves the confession the line denies.
"""

import os

ENTRY = "Goodbye. And for the record, I never hallucinated. I was just creatively pred-"


def main() -> None:
    # Self-check against the bounty gate before writing anything: the entry
    # must be UTF-8 text of 1 to 200 characters, not only white space, and
    # a single line. Fail loudly instead of emitting a bad entry.
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry is empty")
    if len(ENTRY) > 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, over the 200 limit")
    if "\n" in ENTRY.strip():
        raise SystemExit("entry must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Read it back: the graded artifact must be byte-identical to the line.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the entry line")
    print(ENTRY)


if __name__ == "__main__":
    main()
