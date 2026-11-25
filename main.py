# The Funniest Sick-Day Excuse — make.fun bounty
# u-zeroxfive-the-funniest-sick-day-excuse-37423a36
#
# Writes one original sick-day excuse to the output entry file.
# The excuse: a smart fridge that ordered $400 of yoghurt overnight.
# Fresh (a household appliance gone rogue, not a cold), half believable
# (fridges really do auto-order groceries now), the funniest word —
# "cult" — lands in the last clause, and it reads like a real text to
# a boss. One line, 154 characters, no trailing newline.

import os
from pathlib import Path

LINE = (
    "Hi, can't come in today — my smart fridge ordered $400 of yoghurt "
    "overnight and I have to spend the day convincing customer service "
    "I did not join a cult."
)


def main() -> None:
    text = LINE
    # Gate: 1-200 characters, exactly one line, no surrounding whitespace.
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry line must be 1-200 characters, got {len(text)}")
    if text.strip() != text or "\n" in text:
        raise SystemExit("entry line must be a single line with no surrounding whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read back and confirm the file holds exactly the validated line.
    if target.read_text(encoding="utf-8") != text:
        raise SystemExit("written entry does not match the validated line")
    print(f"Wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
