# Contributing

## The Filter

Every contribution must pass: **does it still work after being fully
explained to the other person?**

Manipulation fails the filter by definition. Honest influence passes.

## Rules for new skills

1. Format: `<skill-name>/SKILL.md` with YAML frontmatter (`name`,
   `description` starting with "Use this when...").
2. Plain English. Short sentences. A smart 12-year-old should follow it.
3. Structure: The Big Idea -> The Moves (with example lines) -> When It
   Backfires -> One-Line Memory.
4. No copyrighted text from any book. Original phrasing only. Naming a book
   or author as inspiration is fine.
5. Every example line must be usable in a real chat thread, under 4 lines.
6. Max ~120 lines per skill.

## Process

1. Open an issue describing the mechanism and which situation it solves.
2. PR with the new skill folder + README table row.
3. CI validates frontmatter automatically.

## Lint locally

```bash
python3 scripts/lint.py
```
