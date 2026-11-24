#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty
u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.

Writes a single line (at most 120 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output): the error message a
kitchen toaster shows its owner when something goes wrong.

Pure standard library; deterministic — the same bytes on every run.
"""

import os
import sys

# The entry: a deadpan appliance error. The toaster has detected the one
# pastry it was never built to toast, and it declines — politely, finally,
# and in the flat voice of a machine that has read its own manual. The
# joke lands on a single read: a real-looking error code, a specific
# intruder (not a pun on toast), and a refusal that holds one voice.
LINE = "ERROR E-02: CROISSANT DETECTED. I REFUSE TO PARTICIPATE."

MAX_CHARS = 120


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if line != line.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the bytes we wrote.
    with open(path, "rb") as f:
        if f.read() != data:
            print("verification failed: entry.txt differs", file=sys.stderr)
            return 1
    print(f"wrote {len(data)} bytes ({len(line)} chars) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
