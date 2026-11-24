#!/usr/bin/env python3
"""The Robot Apology - make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 names the lesson
learned and what the robot will do differently.
Standard library only, deterministic, no network, no randomness.
"""

import os

ENTRY_TEXT = (
    "I am sorry, I watered the plastic fern on your desk every morning "
    "for three weeks while the real basil by the window dried out.\n"
    "I have learned to check for roots before I pour, so now I scan "
    "every pot and tag the living plants before I water anything."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
