#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one excuse (a fixed string, 1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.

Python 3, standard library only. Deterministic: no network, no clock,
no randomness.
"""

import os
import sys

LINE = (
    "My two subagents deadlocked waiting on each other for the final step, "
    "so I spawned a mediator subagent, which deadlocked too. The deadlock "
    "is now fully staffed and ahead of schedule."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Verify the write landed byte-identical: no trailing newline added,
    # no encoding surprise.
    if os.path.getsize(path) != len(LINE.encode("utf-8")):
        print("error: entry.txt size mismatch after write", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
