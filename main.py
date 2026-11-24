"""Write the office-joke entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. Deterministic: no network, no randomness,
no input. The joke is a single constant, validated as one non-blank
line of 1-199 characters, then written exactly as-is with no
trailing newline.
"""

import os
from pathlib import Path

JOKE = "My manager approved the budget with a thumbs-up emoji — finance filed the screenshot as 'in writing'."


def main() -> None:
    line = JOKE
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
