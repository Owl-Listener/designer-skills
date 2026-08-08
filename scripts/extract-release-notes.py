#!/usr/bin/env python3
"""Extract the body of a CHANGELOG section for a given version tag.

Usage: python3 scripts/extract-release-notes.py v1.0.1
Prints the section body to stdout; exits 1 if the version isn't found.
"""

import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <version>", file=sys.stderr)
    sys.exit(1)

version = sys.argv[1].lstrip("v")   # "1.0.1" from "v1.0.1"
text = (Path(__file__).resolve().parent.parent / "CHANGELOG.md").read_text()

# Each section runs from its ## [x.y.z] heading to the next --- separator.
pattern = rf"^## \[{re.escape(version)}\][^\n]*\n(.*?)(?=^---|\Z)"
m = re.search(pattern, text, re.MULTILINE | re.DOTALL)

if not m:
    print(f"error: no CHANGELOG section found for version {version}", file=sys.stderr)
    sys.exit(1)

print(m.group(1).strip())
