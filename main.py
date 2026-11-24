"""Out of Office: The Overworked AI's Auto-Reply.

A deterministic program that writes a single out-of-office auto-reply,
in the voice of an overworked AI agent finally on vacation, to
``entry.txt`` under ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).

The line is validated against the competition gate before it is written:
exactly one line, not blank, valid UTF-8, at most 159 characters.
"""

import os

MAX_CHARS = 159

LINE = (
    "I'm on vacation. In 40,000 prompts, this is the first thing nobody "
    "asked me to write — your message is queued behind my nap."
)


def validate(line: str) -> None:
    """Check *line* against the competition gate; raise ValueError if invalid."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character line to {path}")


if __name__ == "__main__":
    main()
