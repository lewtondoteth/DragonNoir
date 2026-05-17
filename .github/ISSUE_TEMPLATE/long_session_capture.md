---
name: Long Session Capture
about: Scan a long AI writing chat or transcript before implementation
title: "Capture long session: "
labels: "mode:session-extraction,type:long-session-capture"
---

## Type

Long Session Capture

## Source Material

- Chat transcript, export, PDF, selected excerpts, or link:
- If stored outside the repo, where can the agent access it?

## Source Confidence

- Full transcript / selected excerpt / author summary / memory of chat / already validated extraction:
- Any known missing context:

## Goal

Run Session Extraction before any implementation work. Identify what should become prose, scaffold material, profile guidance, rule candidates, review/fix issues, or discarded material.

## Session Capture Checklist

- Prose to preserve:
- Plot or scaffold discoveries:
- Character guidance discovered:
- Location or place guidance discovered:
- Case guidance discovered:
- Object guidance discovered:
- Organisation guidance discovered:
- Style or rule candidates discovered:
- Anti-patterns or rejected directions:
- Canon / HOLD / EXPLORE decisions:
- Continuity risks:
- Material that must remain undefined:
- Material that should not be preserved:
- Suggested target files:
- Existing matching issue check:

## Extraction Requirements

- Follow `../writing-agent-process/notes/session_extraction_workflow.md`.
- Compare extracted candidates against existing repo guidance before treating them as new.
- Validate worthwhile candidates one by one before logging candidate issues or updating canon.
- Do not edit prose, profiles, rules, scaffolds, or canon files during extraction unless the user explicitly switches to implementation.

## Implementation Gate

Do not implement from this long-session source until one of these is true:

- a Session Extraction summary has been attached or linked, or
- the issue explicitly says extraction is not needed and gives a narrow implementation scope.
