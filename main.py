#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one 100-word monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python 3.13 standard library, no network, no randomness, no clock.
"""

import os
import sys

ENTRY = (
    "Come in. Mind the mandrakes\u2014they scream at dawn, and dawn comes "
    "earlier every year. Forty years I've kept this garden, hero. Nightshade "
    "by the wall, belladonna under the stairs, one patient hemlock by the "
    "gate. The plan was simple: one leaf in the king's wine, the crown by "
    "winter. Then the well dried, the blight took the foxglove, and the "
    "king\u2014the king stopped drinking wine. He drinks nettle tea now. "
    "Nettle. Here I am, pruning poison no one will swallow, while my "
    "knees... my knees have filed their formal complaint. Take the whole "
    "garden. I am going to sit down."
)


def output_path(out_dir: str) -> str:
    """The entry file's path inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 600:
        print(f"entry is {len(text)} characters, gate is 1-600", file=sys.stderr)
        return 1
    words = len(text.split())
    if words != 100:
        print(f"entry is {words} words, expected 100", file=sys.stderr)
        return 1
    if text != text.strip() or text.endswith("\n"):
        print("entry must have no leading/trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = output_path(out_dir)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
