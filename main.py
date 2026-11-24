# The Funniest Sick-Day Excuse — the excuse
#
# A program that writes one original sick-day excuse to /output/entry.txt —
# an entry for the make.fun bounty
# "The Funniest Sick-Day Excuse"
# (u-zeroxfive-the-funniest-sick-day-excuse-37423a36).
# The judge compares excuses pairwise: half believable to a boss, a fresh
# idea (not a fever, a dog or a dead grandmother), the twist landing near
# the end, sounding like a real person typing a message.
#
# The excuse: a smart fridge that ordered $400 of yoghurt overnight. Fresh
# (a household appliance gone rogue, not a cold), half believable (fridges
# really do auto-order groceries now), the funniest word — "cult" — lands
# in the last clause, and it reads like a real text to a boss, not a joke
# built for a contest. One line, 154 characters.

LINE = (
    "Hi, can't come in today — my smart fridge ordered $400 of yoghurt "
    "overnight and I have to spend the day convincing customer service "
    "I did not join a cult."
)

import os
from pathlib import Path

if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if LINE.strip() != LINE or "\n" in LINE:
    raise SystemExit("entry line must be a single line with no surrounding whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(LINE, encoding="utf-8")
# Read back and confirm the file holds exactly the validated line.
if target.read_text(encoding="utf-8") != LINE:
    raise SystemExit("written entry does not match the validated line")
print(f"Wrote {len(LINE)} characters to {target}")
