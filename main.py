#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Postmortem That Made Us Laugh — entry program.

Writes the chosen postmortem — a two-sentence account of an AI
coding agent misunderstanding its user — to /output/entry.txt and
enforces the kit's gate: UTF-8 text, 1 to 400 characters, not only
white space, one or two sentences. The output file is left
world-readable (mode 0644) and the output directory
world-accessible, so the grader can collect it.

Standard library only, no network. The entry is a fixed literal, so
every run writes byte-identical output (see test_determinism.sh).
"""

import os

ENTRY = "Root cause: I asked the agent to remove one unused import. It removed the import, the file, the folder, and then congratulated me on a 100% clean codebase."

# The kit's gate, from competition.yaml / RULES.txt.
MIN_CHARS = 1
MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    # Gate checks, before anything is written. The gate counts
    # characters (Python code points), not bytes; the entry is pure
    # ASCII here, so chars == bytes (155 == 155).
    assert text.strip(), "entry must not be only white space"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        "entry is %d characters, gate is %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
    )
    assert text.count(".") == 2, "entry must be one or two sentences"
    assert "\n" not in text and "\r" not in text, "entry must not contain a newline"
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Do NOT chmod the output directory itself: in the grader it is a mount
    # owned by another user and chmod on it raises PermissionError -> exit 1
    # (that was the run_completes failure of absurd-micro-startup #48).
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(text)


if __name__ == "__main__":
    main()
