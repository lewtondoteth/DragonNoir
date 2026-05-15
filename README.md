# Dragon Noir

This repository contains the standalone Toy Noir Dragon book project.

It is now dedicated to the noir continuity only. The family Dragon project remains in the old `Dragon-Stories` repository history and should not be used as guidance here unless explicitly provided again for comparison or adaptation.

## AI / Agent Context

AI assistants and coding agents should read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`

`AGENTS.md` contains the short bootstrap instruction for agent workflows.

## Authoritative Reference

- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- `rules/noir_narration_rules.md`
- `characters/pink_dragon_character_profile.md`
- `locations/Toy_City_location_profile.md`
- `locations/Dragon_Office_location_profile.md`

## File Index

```text
DragonNoir/
├── AGENTS.md
├── AI_REPO_CONTEXT.md
├── README.md
├── chapters/
│   ├── README.md
│   └── chapter_01_opening.md
├── characters/
│   └── pink_dragon_character_profile.md
├── discarded_or_experimental/
│   └── README.md
├── locations/
│   ├── README.md
│   ├── Dragon_Office_location_profile.md
│   └── Toy_City_location_profile.md
├── notes/
│   ├── README.md
│   ├── development_options.md
│   ├── issue_workflow.md
│   ├── mode_preflight_workflow.md
│   ├── opening_case_music_box_scaffold.md
│   ├── profile_scan_workflow.md
│   ├── repo_manifest.json
│   ├── repo_manifest.md
│   ├── repo_connection_workflow.md
│   ├── scaffold_capture_workflow.md
│   ├── rule_validation_workflow.md
│   ├── session_extraction_workflow.md
│   └── writing_workflow.md
├── outlines/
│   └── chapter_01_narrative_beats.md
├── rules/
│   └── noir_narration_rules.md
├── scenes/
│   ├── README.md
│   └── chapter_01_office_entry_coffee_ritual_draft.md
├── story_bible/
│   ├── README.md
│   ├── Toy_Noir_Dragon_AI_Prompt_Pack.md
│   └── Toy_Noir_Dragon_Standalone_Story_Bible.md
└── tools/
    ├── README.md
    └── generate_repo_manifest.py
```

## Working Structure

- `chapters/` — canonical or assembled chapter drafts
- `scenes/` — scene drafts, fragments, and scene-level experiments
- `outlines/` — chapter architecture, narrative beats, and pacing references
- `characters/` — canonical character profiles and expanded continuity notes
- `locations/` — canonical location profiles and expanded place-continuity notes
- `rules/` — canonical practical writing rules discovered during drafting
- `discarded_or_experimental/` — retired alternatives and preserved non-canonical material
- `notes/` — planning notes, continuity tracking, mystery structure, and revision notes
- `story_bible/` — authoritative noir project bible and prompt pack
- `tools/` — small maintenance helpers for manifest generation and repo upkeep

## Chapter 1 Workflow

- Canonical current draft: `chapters/chapter_01_opening.md`
- Canonical pacing reference: `outlines/chapter_01_narrative_beats.md`
- Current experimental scene sandbox: `scenes/chapter_01_office_entry_coffee_ritual_draft.md`
- Practical narration rules: `rules/noir_narration_rules.md`
- Opening-case scaffold: `notes/opening_case_music_box_scaffold.md`
- Issue workflow: `notes/issue_workflow.md`

Keep canonical prose, experimental scene drafts, and structural outlines separate while drafting.

## Chapter Status

Use this table to understand what each major story artifact is for before editing or reviewing it.

| Item | File | Status | Use for | Notes |
| --- | --- | --- | --- | --- |
| Chapter 1 opening | `chapters/chapter_01_opening.md` | Active canonical draft | Main Chapter 1 prose | Treat as the current assembled chapter unless the user says otherwise. |
| Chapter 1 narrative beats | `outlines/chapter_01_narrative_beats.md` | Active canonical structure | Pacing, sequence, and scene-function reference | Use to check whether new prose still follows the intended opening movement. |
| Office-entry coffee ritual | `scenes/chapter_01_office_entry_coffee_ritual_draft.md` | Experimental scene study | Texture, pacing, and possible integration material | Do not treat as canonical prose unless integrated into the active chapter. |
| Opening-case music box scaffold | `notes/opening_case_music_box_scaffold.md` | Provisional planning | Possible opening-case shape | Not fixed canon; promote only by explicit user request or canon-promotion issue. |
| Development options | `notes/development_options.md` | Retired/exploratory notes | Backup ideas and comparison material | Not active canon unless explicitly revived. |

When adding, removing, renaming, or changing the status of a major chapter, scene, outline, or planning artifact, update this table in the same change.

## Current Active Drafts

- `chapters/chapter_01_opening.md` — canonical current Chapter 1 draft. Contains the rain/city opening, Dragon's trifle-hangover state, doorway reveal, office-entry transition, coffee sequence, and layered recognition progression.

## Scene Studies

- `scenes/chapter_01_office_entry_coffee_ritual_draft.md` — experimental office-entry and coffee material. Retained as a scene-study sandbox; do not treat as canonical prose unless integrated into `chapters/chapter_01_opening.md`.

## Outlines And Notes

- `outlines/chapter_01_narrative_beats.md` — canonical Chapter 1 pacing and architecture reference.
- `locations/Toy_City_location_profile.md` — canonical setting profile for Toy City atmosphere, scale, and city logic.
- `locations/Dragon_Office_location_profile.md` — canonical location profile for Dragon's office as recurring scene space.
- `notes/issue_workflow.md` — GitHub issue handoff workflow, issue types, and acceptance criteria.
- `notes/mode_preflight_workflow.md` — shared preflight for manifest refresh, scoped file loading, and open-issue dedupe before mode work.
- `notes/repo_connection_workflow.md` — front-door workflow for connecting to the repo, orienting, and routing into the correct work mode.
- `notes/repo_manifest.json` — generated machine-readable repo index for agent orientation.
- `notes/repo_manifest.md` — generated human-readable repo index for agent orientation.
- `notes/profile_scan_workflow.md` — workflow for a manual profile pull from prose, extracting durable character-profile, location-profile, and spatial guidance from draft text.
- `notes/scaffold_capture_workflow.md` — workflow for capturing plot directions and scaffolds as provisional planning while separating out reusable knowledge.
- `notes/session_extraction_workflow.md` — provisional workflow for extracting reusable writing knowledge from shared ChatGPT sessions or exported logs.
- `notes/rule_validation_workflow.md` — provisional workflow for validating extracted or existing rules one by one before canon updates.
- `notes/writing_workflow.md` — drafting workflow that forces chapter/scene/character context retrieval before prose generation.
- `notes/opening_case_music_box_scaffold.md` — exploratory stolen music box opening-case scaffold. Not fixed canon.
- `notes/development_options.md` — retired, backup, and exploratory ideas. Not active canon unless explicitly revived.
- `tools/generate_repo_manifest.py` — regenerates the repo manifest so agent orientation scales as files and modes are added.

## Issue Workflow

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

Issue workflow reference:

- `notes/issue_workflow.md`

When asking an AI agent to "log a ticket", "log an issue", "create an issue", or "make a ticket", the agent should create a GitHub issue using the appropriate template and should not edit repository files unless implementation is separately requested.

For `Session Extraction` and `Profile Pull`, the default preservation path is:

1. extract and classify findings
2. validate them one by one
3. log the approved result as the appropriate issue type

Do not treat extraction approval by itself as permission to directly update canon files unless the user explicitly switches into implementation or direct canon-update work.

Before logging any new issue in Review, Session Extraction, Profile Pull, Character Scan, Consistency Scan, Writing follow-up logging, or Scaffold Capture, check whether the same scope is already tracked by an open issue and reuse it instead of creating a duplicate.

Implementation agents should treat issues as scoped instructions, not permission to broadly rewrite. Review issues use the read-only AI Review Path. Planning/scaffold issues stay provisional unless the issue explicitly says to promote material into canon.

When logging a new issue, use the templates in `notes/issue_workflow.md` for implementation, review, planning/scaffold, canon promotion, and follow-up issues.

Before closing an implementation issue, check the acceptance criteria in `notes/issue_workflow.md`, including scope control, canon/provisional boundaries, README/path updates, prose style, character continuity, post-implementation style/flow conflicts, and `git diff --check`.

If the scoped work is complete but a criterion or style/flow check exposes a real out-of-scope problem, the agent should allow the implementation through and create a follow-up issue explaining what is wrong and how it might be resolved.

## Session Extraction Flow

Use `Session Extraction` as a separate repo role after a drafting chat is finished.

The intended flow is:

1. have the drafting conversation elsewhere
2. provide the chat log, export, transcript, or attached PDF to the repo-connected agent
3. switch into `Session Extraction`
4. let the extraction agent analyze the session for durable knowledge
5. validate any worthwhile findings one by one
6. log approved candidates as issues unless direct implementation is explicitly requested

This keeps prose generation and post-writing extraction as distinct activities with different goals.

## Profile Pull Flow

Use `Profile Pull` when the useful profile knowledge is already embodied in prose and should be extracted from the draft itself rather than from a chat export.

This mode also covers `Character Scan` work: reading prose to extract durable character guidance and to check for clashes against the current character or location profiles.

`Consistency Scan` is an accepted alias when the main goal is to compare prose against the current rules, character profiles, and location profiles and then log any needed fix issues.

The intended flow is:

1. provide the prose, scene, chapter, or passage
2. switch into `Profile Pull`
3. let the agent separate durable profile guidance from local scene staging
4. validate any character-profile, location-profile, or spatial-guidance findings one by one
5. log approved profile candidates as issues unless direct implementation is explicitly requested
6. if the scan finds a clash or inconsistency, identify it clearly, ask any needed clarification questions one at a time, and log a fix issue unless direct implementation is explicitly requested

## Shared Mode Preflight

Use `notes/mode_preflight_workflow.md` before mode-specific work when the scope is non-trivial, the repo tree has changed, or issue dedupe matters.

The preflight should:

1. refresh the repo manifest with `python3 tools/generate_repo_manifest.py` when needed
2. load the minimum relevant files for the current scope
3. check for already-open matching issues
4. give a short mode-specific orientation summary before proceeding

## Drafting-State Protocol

Use `[EXPLORE]`, `[HOLD]`, and `[CANON]` to prevent exploratory drafting material from becoming accidental continuity.

Before issue logging, file updates, lore updates, PRs, or summaries that may become handoff material, verify what has actually been approved as canon. If uncertain, generalise the material and avoid promoting provisional names, organisations, artifacts, case terms, or plot mechanics.

## Canonical vs Experimental

- Canonical: story bible, narration rules, character profiles, location profiles, active chapter drafts, and active outline references.
- Development: notes and opening-case scaffolds that preserve possibilities without locking plot.
- Experimental: scene sandboxes and pacing studies.
- Retired: discarded or backup ideas preserved for later comparison or revival.

## AI Review Path

When asking an AI agent to review, critique, assess, audit, or give feedback, the agent should use a read-only review path.

Review mode means:

- do not edit story files
- do not resolve issues directly
- compare the requested material against the story bible, prompt pack, narration rules, character profiles, location profiles, and relevant outlines/notes
- log detailed issues with reasons and suggested resolution directions

Review should focus especially on:

- pacing and feel of the prose
- whether the passage matches Dragon's first-person noir voice
- whether the tone stays internally consistent across the passage
- consequence-first narration instead of flat stage directions
- implication-heavy emotional movement
- toy-world play-as-reality logic
- character consistency, motives, and action logic against the current character files
- location consistency and stable spatial logic against the current location files
- canon/provisional boundaries
- factual continuity inside the draft
- scene function and structural flow

An issue report should explain where the problem appears, why it conflicts with the repo's rules or story logic, how it affects pacing/feel/continuity/character, and what kind of revision would resolve it.

When review uncovers a likely conflict, gap, or unresolved inconsistency, the normal repair path is:

1. identify the issue clearly
2. ask any needed clarification questions one at a time
3. allow correction before locking the diagnosis
4. log the issue for later implementation unless the user explicitly asks to fix it now

Agents should not rewrite the passage during review unless the user explicitly asks for implementation after the review.

## Active Canon

The active canon is Dragon, the pink dragon, Toy City, narration style, repair logic, treasure instinct, rain logic, play-as-reality toy ontology, and the emotional/thematic dynamics between the two dragons.

The exact case, mystery engine, artifact, antagonist, and ending structure are provisional until deliberately promoted into the story bible.

Retired/provisional noir plot material, including the Ember-Stone, Patchwork Guardian, wind-up mouse courier, and related fixed-plot machinery, belongs in development notes and should not be treated as active canon unless explicitly revived.
