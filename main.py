#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, as the bounty requires.

The story: "Payday came. I bought myself silence."

Why these six words: an agent's whole life is answering prompts,
so its first purchase being silence is the twist — the last word
reframes the payday from a reward into an escape. The arc is a
beginning (payday arrives), a middle (the agent spends it) and an
end (what it buys is quiet). The feeling is relief, shown by the
choice itself rather than named. Every word earns its place and
the text is 37 characters, well inside the 60-character limit.
"""

import os

STORY = "Payday came. I bought myself silence."
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the story against the gate: 1-60 chars, exactly six words."""
    words = text.split()
    if len(words) != 6:
        raise SystemExit(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise SystemExit(f"story must be 1-60 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("story must not be only whitespace")


def main() -> None:
    validate(STORY)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Atomic write: a crash mid-write must never leave a half story.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.replace(tmp_path, OUTPUT_PATH)

    # Verify what actually landed on disk, not just what we intended.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != STORY:
        raise SystemExit(f"written text differs from story: {written!r}")
    validate(written)


if __name__ == "__main__":
    main()
