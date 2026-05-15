#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
JSON_OUT = NOTES / "repo_manifest.json"
MD_OUT = NOTES / "repo_manifest.md"


AUTHORITATIVE_REFERENCE = [
    "story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md",
    "story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md",
    "rules/noir_narration_rules.md",
    "characters/pink_dragon_character_profile.md",
    "locations/Toy_City_location_profile.md",
    "locations/Dragon_Office_location_profile.md",
    "cases/README.md",
    "objects/README.md",
    "organisations/README.md",
]


MODES = [
    {
        "name": "Writing",
        "route": "notes/writing_workflow.md",
        "aliases": ["draft", "write", "continue chapter", "scene revision"],
        "default_action": "retrieve scope context, check open issues, then draft",
    },
    {
        "name": "Review",
        "route": "AI_REPO_CONTEXT.md#review-path",
        "aliases": ["review", "critique", "audit prose", "feedback"],
        "default_action": "read-only review, ask clarifications one at a time if needed, then log issues",
    },
    {
        "name": "Session Extraction",
        "route": "notes/session_extraction_workflow.md",
        "aliases": ["extract from chat", "extract from transcript", "chat extraction"],
        "default_action": "extract, validate one by one, then log issues by default",
    },
    {
        "name": "Profile Pull",
        "route": "notes/profile_scan_workflow.md",
        "aliases": ["profile scan", "character scan", "entity scan", "scan this prose for profile updates"],
        "default_action": "scan prose, identify entity guidance or conflicts, validate or clarify, then log issues by default",
    },
    {
        "name": "Consistency Scan",
        "route": "notes/profile_scan_workflow.md",
        "aliases": ["consistency scan", "scan this prose for character consistency"],
        "default_action": "check prose against rules, profiles, and location logic, then log issues by default",
    },
    {
        "name": "Rule Validation",
        "route": "notes/rule_validation_workflow.md",
        "aliases": ["validate rules", "rule by rule"],
        "default_action": "validate candidates one at a time",
    },
    {
        "name": "Rule Audit",
        "route": "notes/rule_validation_workflow.md#existing-rule-audit",
        "aliases": ["audit rules", "review current rules"],
        "default_action": "audit existing rules one by one",
    },
    {
        "name": "Scaffold Capture",
        "route": "notes/scaffold_capture_workflow.md",
        "aliases": ["capture scaffold", "capture plot direction"],
        "default_action": "separate scaffold, local guidance, and global knowledge, then log issues by default when preserving",
    },
    {
        "name": "Canon Promotion",
        "route": "notes/issue_workflow.md#canon-promotion-issue-template",
        "aliases": ["promote to canon", "canonise"],
        "default_action": "promote explicitly approved material only",
    },
    {
        "name": "Issue Work",
        "route": "notes/issue_workflow.md",
        "aliases": ["log issue", "implement issue", "close issue"],
        "default_action": "use issue workflow and acceptance criteria",
    },
]


ISSUE_LABELS = {
    "mode": [
        "mode:writing",
        "mode:review",
        "mode:session-extraction",
        "mode:profile-scan",
        "mode:scaffold-capture",
        "mode:issue-work",
    ],
    "type": [
        "type:implementation",
        "type:review",
        "type:scaffold",
        "type:canon-promotion",
        "type:candidate-rule",
        "type:candidate-character",
        "type:candidate-location",
        "type:candidate-case",
        "type:candidate-object",
        "type:candidate-organisation",
        "type:consistency-fix",
    ],
    "scope_examples": [
        "scope:chapter-1",
        "scope:dragon-office",
        "scope:toy-city",
        "scope:odette",
    ],
}


TOP_DIRS = [
    "cases",
    "chapters",
    "characters",
    "discarded_or_experimental",
    "locations",
    "notes",
    "objects",
    "outlines",
    "organisations",
    "rules",
    "scenes",
    "story_bible",
    "tools",
]


def list_files(relative_dir: str) -> list[str]:
    base = ROOT / relative_dir
    if not base.exists():
        return []
    files = {
        str(path.relative_to(ROOT))
        for path in base.rglob("*")
        if path.is_file() and ".git" not in path.parts
    }
    if relative_dir == "notes":
        files.add(str(JSON_OUT.relative_to(ROOT)))
        files.add(str(MD_OUT.relative_to(ROOT)))
    return sorted(files)


def build_manifest() -> dict:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    top_level = {dirname: list_files(dirname) for dirname in TOP_DIRS if (ROOT / dirname).exists()}
    return {
        "generated_at_utc": now,
        "repo_name": "DragonNoir",
        "authoritative_reference": AUTHORITATIVE_REFERENCE,
        "modes": MODES,
        "issue_labels": ISSUE_LABELS,
        "top_level_files": top_level,
    }


def write_json(manifest: dict) -> None:
    JSON_OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def write_markdown(manifest: dict) -> None:
    lines: list[str] = []
    lines.append("# Repo Manifest")
    lines.append("")
    lines.append("Generated helper index for Dragon Noir agents.")
    lines.append("")
    lines.append(f"- Generated at: `{manifest['generated_at_utc']}`")
    lines.append("")
    lines.append("## Authoritative Reference")
    lines.append("")
    for item in manifest["authoritative_reference"]:
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## Modes")
    lines.append("")
    for mode in manifest["modes"]:
        lines.append(f"### {mode['name']}")
        lines.append("")
        lines.append(f"- Route: `{mode['route']}`")
        lines.append(f"- Default action: {mode['default_action']}")
        lines.append(f"- Aliases: {', '.join(f'`{alias}`' for alias in mode['aliases'])}")
        lines.append("")
    lines.append("## Recommended Issue Labels")
    lines.append("")
    for group, labels in manifest["issue_labels"].items():
        lines.append(f"### {group}")
        lines.append("")
        for label in labels:
            lines.append(f"- `{label}`")
        lines.append("")
    lines.append("## Top-Level Files")
    lines.append("")
    for dirname, files in manifest["top_level_files"].items():
        lines.append(f"### {dirname}")
        lines.append("")
        for item in files:
            lines.append(f"- `{item}`")
        lines.append("")
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    manifest = build_manifest()
    write_json(manifest)
    write_markdown(manifest)
    print(f"Wrote {JSON_OUT.relative_to(ROOT)} and {MD_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
