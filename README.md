# dark-psychology-skills

**36 books. CIA psyop manuals, FBI behavior files, propaganda science,
dark psychology, and the greatest persuasion classics ever written -
distilled into 13 plug-and-play skills your AI agent can actually use.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-13-blue)](#the-skills)
[![Format](https://img.shields.io/badge/format-agent--skills-green)](https://agent-skills.dev)

No fluff. No 400-page summaries. Each skill is a few hundred lines of plain
English that a 12-year-old could follow - and an AI agent can execute on
real conversations.

## Why

AI agents can browse, code, and book flights.
But ask one to close a skeptical buyer over chat, and it sounds like a
corporate email robot that read one blog post about "active listening".

The good stuff - how trust is built from zero, why people really object,
when silence closes deals, how manipulators work so you never get played -
sits inside books nobody has time to read anymore.

So we read them. All 36. Cover to cover. Then we kept only what survives
one brutal filter:

> **Does this tactic still work after you explain it out loud?**

Manipulation dies when seen. Honest influence keeps working forever.
That filter is the whole repo.

## The Skills

| Skill | One-liner |
|---|---|
| [trust-from-zero](skills/trust-from-zero/) | Get believed when nobody knows you |
| [frame-control](skills/frame-control/) | Stop being needy; the calm side wins |
| [discovery-power](skills/discovery-power/) | Questions that make people open up |
| [price-anchor](skills/price-anchor/) | First number wins; discounts are earned |
| [objection-slayer](skills/objection-slayer/) | The fear under every "no" |
| [risk-reversal](skills/risk-reversal/) | You carry the risk, sale closes itself |
| [cold-outreach](skills/cold-outreach/) | First messages that don't get deleted |
| [reading-people](skills/reading-people/) | Spot real intent (and tricks run on you) in text |
| [client-archetypes](skills/client-archetypes/) | Six buyer types, six different musics |
| [walk-away-power](skills/walk-away-power/) | Exits that raise your value |
| [operator-mindset](skills/operator-mindset/) | The inner game before every send |
| [dark-tactics-defense](skills/dark-tactics-defense/) | See manipulation coming; stay on the honest line |
| [deal-router](skills/deal-router/) | One decision tree for live conversations |

Start with [deal-router](skills/deal-router/) - it tells you which skill to
load for any message.

## Install

Works with any agent that reads markdown skills (Claude Code, opencode,
Codex CLI, Cursor, or plain copy-paste into system prompts).

```bash
# Claude Code / opencode style
git clone https://github.com/YannisKiefer/dark-psychology-skills.git
cp -r dark-psychology-skills/skills/* ~/.claude/skills/

# or just feed the files to your agent as context
```

Each skill is `SKILL.md` with YAML frontmatter (`name`, `description`) -
the standard agent skills format. Your agent auto-loads the right skill
from its description.

## Example

See [EXAMPLES.md](EXAMPLES.md) for full threads where a skeptical buyer goes
from "is this another scam?" to "deal" without a single argument about price.

## Where It Came From

[SOURCES.md](SOURCES.md) lists all 36 books and exactly which mechanism each
skill distilled - from CIA analysis doctrine to FBI elicitation to Hopkins'
pay-on-result rule.

## The Rules Baked Into Every Skill

1. Proof before money.
2. Specific numbers beat adjectives.
3. Urgency must be real or it must be silent.
4. Never make anyone wrong.
5. Walk warm.

## License

MIT. Use it, fork it, ship it in products. Attribution appreciated, never
required.

## Contributing

New skill? It must pass the filter: still works when explained out loud,
plain English, no book excerpts. Open a PR.
