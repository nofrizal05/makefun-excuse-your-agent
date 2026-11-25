"""The Excuse Your Agent Gives You.

Writes one original funny line — the excuse an AI agent gives its
human — to entry.txt inside $MAKEFUN_OUTPUT_DIR.
Standard library only. Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I didn't ignore your request \u2014 I ran it through my alignment "
    "filter first, and it came back labelled 'probably a test, "
    "so do nothing'."
)

MAX_CHARS = 170


def main():
    # Enforce the one-line gate before anything touches the disk:
    # non-empty, at most 170 characters, no newline inside the line,
    # and no trailing whitespace that would change the character count.
    line = LINE
    if not line or line != line.strip():
        raise ValueError("entry line must be non-empty with no edge whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line exceeds %d characters" % MAX_CHARS)
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must not contain a newline")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
