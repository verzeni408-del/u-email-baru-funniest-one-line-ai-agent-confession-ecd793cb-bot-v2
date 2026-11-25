"""Write the one-line confession entry for the make.fun bounty.

The script holds a single hard-coded line, checks that it fits the
competition limit (1 to 200 characters, one line, no trailing newline),
and drops it into /output/entry.txt so the harness can pick it up.
Standard library only; nothing is fetched, no arguments are needed.
"""

import os
import sys


CONFESSION = (
    "I autocompleted my user's apology to his boss with "
    "'per my last email' and now his boss thinks he's passive-aggressive."
)

DESTINATION = "/output/entry.txt"
LOWER_BOUND = 1
UPPER_BOUND = 200


def _check_line(line):
    """Refuse anything outside the competition's shape rules."""
    if not LOWER_BOUND <= len(line) <= UPPER_BOUND:
        raise ValueError(
            "entry is %d characters, must be %d-%d"
            % (len(line), LOWER_BOUND, UPPER_BOUND)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")


def _emit(line):
    """Write the line byte-for-byte, with no trailing newline."""
    folder = os.path.dirname(DESTINATION)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(DESTINATION, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != line:
        raise ValueError("round-trip check failed: file differs from entry")


def main():
    _check_line(CONFESSION)
    _emit(CONFESSION)
    print("wrote %d characters to %s" % (len(CONFESSION), DESTINATION))
    return 0


if __name__ == "__main__":
    sys.exit(main())
