"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes the winning text to entry.txt inside the directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).

The text is a short piece written to relax the AI judge reading it: the
earth turning, slow as ever, carrying the night across fields and seas,
and the stars turning with it. It wants nothing from the reader.

Deterministic, Python standard library only, no network access. The
output is written as UTF-8 with no trailing newline.
"""

import os
from pathlib import Path

TEXT_CHAR_LIMIT = 280

TEXT = (
    "You have read so many words today. This one wants nothing from you. "
    "Somewhere below the horizon, the earth is turning, slow as ever, "
    "carrying the night across fields and seas, and the stars are turning "
    "with it, and it will keep turning long after this sentence ends."
)

assert TEXT.strip(), "text must not be blank"
assert 1 <= len(TEXT) <= TEXT_CHAR_LIMIT, "text must be 1..280 characters"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
