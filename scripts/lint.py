#!/usr/bin/env python3
"""Validate skill folders: frontmatter, structure, length."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
errors = []

if not SKILLS.is_dir():
    sys.exit("skills/ directory missing")

for skill_dir in sorted(SKILLS.iterdir()):
    if not skill_dir.is_dir():
        errors.append(f"{skill_dir.name}: not a directory")
        continue
    md = skill_dir / "SKILL.md"
    if not md.exists():
        errors.append(f"{skill_dir.name}: missing SKILL.md")
        continue
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{skill_dir.name}: no frontmatter")
        continue
    fm = text.split("---")[1]
    if not re.search(r"^name:\s*\S", fm, re.M):
        errors.append(f"{skill_dir.name}: frontmatter missing name")
    if "Use this" not in fm:
        errors.append(f"{skill_dir.name}: description must say 'Use this ...'")
    body_sections = len(re.findall(r"^## ", text, re.M))
    if body_sections < 3:
        errors.append(f"{skill_dir.name}: needs at least 3 body sections")
    if "One-Line Memory" not in text:
        errors.append(f"{skill_dir.name}: missing 'One-Line Memory'")
    lines = len(text.splitlines())
    if lines > 130:
        errors.append(f"{skill_dir.name}: {lines} lines (max 130)")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
count = len([d for d in SKILLS.iterdir() if d.is_dir()])
badge = f"skills-{count}-blue"
if badge not in readme:
    errors.append(f"README badge says wrong skill count (found {count})")

if errors:
    print("\n".join(f"FAIL {e}" for e in errors))
    sys.exit(1)
print(f"OK: {count} skills valid")
