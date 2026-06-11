#!/usr/bin/env python3
"""Add a merged PR author to CONTRIBUTORS.md (bots excluded)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRIBUTORS_FILE = ROOT / "CONTRIBUTORS.md"
MAINTAINER = "zshgustavo"

BOT_LOGIN_EXACT = {
    "dependabot",
    "dependabot-preview",
    "dependabot[bot]",
    "dependabot-preview[bot]",
    "github-actions[bot]",
    "renovate[bot]",
    "renovate-bot",
    "imgbot[bot]",
    "sonarcloud[bot]",
    "codecov[bot]",
    "codecov-io",
    "greenkeeper[bot]",
    "mergify[bot]",
    "stale[bot]",
    "copilot",
    "github-copilot[bot]",
    "copilot-swe-agent[bot]",
}

BOT_LOGIN_SUBSTRINGS = (
    "dependabot",
    "copilot",
    "github-actions",
    "renovate",
    "imgbot",
    "sonarcloud",
    "codecov",
    "greenkeeper",
    "mergify",
)

MARKER_START = "<!-- contributors:start -->"
MARKER_END = "<!-- contributors:end -->"


def is_bot(login: str) -> bool:
    normalized = login.strip().lower()
    if not normalized:
        return True
    if normalized in {name.lower() for name in BOT_LOGIN_EXACT}:
        return True
    if normalized.endswith("[bot]"):
        return True
    return any(token in normalized for token in BOT_LOGIN_SUBSTRINGS)


def parse_existing_logins(content: str) -> set[str]:
    logins = set()
    for match in re.finditer(r"\(https://github\.com/([^)]+)\)", content):
        logins.add(match.group(1).lower())
    return logins


def parse_contributor_lines(block: str) -> list[str]:
    lines = [line.rstrip() for line in block.splitlines() if line.strip()]
    return sorted(lines, key=lambda line: line.lower())


def format_contributor_line(login: str) -> str:
    return f"- [{login}](https://github.com/{login})"


def update_contributors(login: str) -> bool:
    login = login.strip()
    if not login:
        print("No login provided; skipping.")
        return False

    if login.lower() == MAINTAINER.lower():
        print(f"Maintainer @{MAINTAINER} is already listed at the top; skipping.")
        return False

    if is_bot(login):
        print(f"Skipping bot/app account: {login}")
        return False

    content = CONTRIBUTORS_FILE.read_text(encoding="utf-8")
    existing = parse_existing_logins(content)

    if login.lower() in existing:
        print(f"Contributor @{login} already listed; skipping.")
        return False

    if MARKER_START not in content or MARKER_END not in content:
        raise SystemExit(f"Markers not found in {CONTRIBUTORS_FILE}")

    before, rest = content.split(MARKER_START, 1)
    block, after = rest.split(MARKER_END, 1)

    lines = parse_contributor_lines(block)
    lines.append(format_contributor_line(login))
    lines = sorted(lines, key=lambda line: line.lower())

    new_block = "\n".join(lines)
    if new_block:
        new_block += "\n"

    updated = f"{before}{MARKER_START}\n{new_block}{MARKER_END}{after}"
    CONTRIBUTORS_FILE.write_text(updated, encoding="utf-8")
    print(f"Added contributor @{login}")
    return True


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: update_contributors.py <github-login>")

    changed = update_contributors(sys.argv[1])
    sys.exit(0 if changed else 0)


if __name__ == "__main__":
    main()