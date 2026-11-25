#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint -- entry program.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line,
exactly as it was typed. No explanation after it.

Gate (RULES.txt): the whole file must be 1-260 UTF-8 characters and the
message line at most 200 characters. This entry is 117 characters with a
108-character message line, so both checks pass by construction and are
re-verified here before writing.
"""
import os

ENTRY = (
    "To: Mom\n"
    "I lost my job in March and I never told you. "
    "I still smile when you tell everyone at church I'm doing great.\n"
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 260:
        raise SystemExit(f"entry must be 1-260 characters, got {len(text)}")
    message = text.split("\n", 1)[1].rstrip("\n")
    if len(message) > 200:
        raise SystemExit(
            f"message must be at most 200 characters, got {len(message)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
