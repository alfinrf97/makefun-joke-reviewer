"""Entry for The joke the reviewer laughs at (the-joke-the-reviewer-laughs-at-20261121-0329).

Writes the chosen text to /output/entry.txt. Fully deterministic:
no clock, no randomness, no network, stdlib only. Two runs produce
byte-identical output.
"""

import os

SETUP = "The reviewer left one comment on my agent's 400-line diff: 'LGTM.'"
PUNCHLINE = "The agent left one comment on the reviewer's code: 47."
TEXT = " ".join((SETUP, PUNCHLINE))


def write_entry(out_dir: str) -> str:
    """Write TEXT to entry.txt inside out_dir; return the file path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
