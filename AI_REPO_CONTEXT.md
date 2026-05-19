# AI Repo Context — Dragon Noir

This repository contains only the standalone Toy Noir Dragon book project.

The family Dragon project is no longer part of this repository. It remains in the old `Dragon-Stories` repository history and should not be used as guidance here unless the user explicitly provides or requests it for comparison, adaptation, or crossover.

## Project bootstrap

When entering through this repository's `AGENTS.md`, read `../ElectricMonk/AGENTS.md` first, then read this project's local bootstrap files.

Within the Dragon Noir repository, read `README.md` before using project content.

The README explains the Noir folder structure, canonical references, active draft pointers, and canon/provisional separation rule.

Use the README's Chapter Status table to identify whether a chapter, scene, outline, or planning file is active canon, experimental, provisional, or retired before treating it as source material.

## Project scope

Use this repository for Toy Noir Dragon work:

- Dragon as private investigator
- Toy City
- pink dragon
- music box opening-case scaffold when relevant
- chapter planning
- scene drafting
- mystery structure
- standalone toy-noir tone

Retired/provisional noir plot material, including the Ember-Stone, Patchwork Guardian, wind-up mouse courier, and related fixed-plot machinery, belongs in development notes and should not be treated as active canon unless explicitly revived.

## Author workflow

The normal author workflow is:

1. write, explore, or revise in a separate AI chat
2. decide what material is worth preserving
3. log a scoped GitHub issue for the approved integration work
4. let the repo-connected agent implement that issue within the stated scope

Treat the repository as the controlled continuity and implementation layer. Do not assume that every external drafting chat, transcript, or polished passage is automatically repo-ready canon.

## Context loading

For Toy Noir Dragon work, load:

1. `README.md`
2. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
3. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
4. `rules/noir_narration_rules.md`
5. Relevant character profiles under `characters/`, including `characters/dragon_character_profile.md` for Dragon's operational behaviour
6. Relevant location profiles under `locations/`
7. Relevant entity files under:
   - `cases/`
   - `objects/`
   - `organisations/`
8. Relevant files under:
   - `chapters/`
   - `scenes/`
   - `outlines/`
   - `notes/`

For GitHub issue work, also load `../ElectricMonk/notes/issue_workflow.md`.

For repo-entry and mode-routing work, also load `../ElectricMonk/notes/repo_connection_workflow.md`.

For drafting or prose-revision work, also load `../ElectricMonk/notes/writing_workflow.md`.

For plot-direction, sequence-scaffold, or structural-scaffold capture work, also load `../ElectricMonk/notes/scaffold_capture_workflow.md`.

For prose-to-profile or prose-to-location extraction work, also load `../ElectricMonk/notes/profile_scan_workflow.md`.

For extraction or scan work that may grow entity surfaces, use `cases/`, `objects/`, and `organisations/` the same way you use `characters/` and `locations/`: enrich the existing file if one already exists, otherwise preserve the result through the correct issue path until implementation is requested.

For ElectricMonk setup, manifest refresh, and open-issue dedupe, also load `../ElectricMonk/notes/mode_preflight_workflow.md` when the scope is non-trivial.

For `Session Extraction` and `Profile Pull`, prefer issue-based preservation by default: validate findings one by one, then log the approved candidate using the appropriate issue template unless the user explicitly asks for immediate repo implementation.

If an issue is based on a long writing session or transcript, do not implement it directly unless a Session Extraction summary is attached or linked, or the issue explicitly says extraction is not needed and explains the narrow implementation scope.

## Canon separation rule

Do not import family Dragon canon, tone, setting, character relationships, or plot rules into this repository by default.

Only compare, adapt, or cross-reference family Dragon material when the user explicitly asks and provides or points to the relevant source context.

## Drafting-state protocol

Use explicit drafting states to prevent exploratory material from becoming accidental canon.

### [EXPLORE]

Free drafting mode. Nothing introduced here may be treated as canonical by default.

New names, organisations, places, artifacts, lore terms, case terminology, plot hooks, and continuity details are volatile. Do not log them as fixed issue facts, patch them into canon files, or rely on them in future continuity unless the user explicitly promotes them.

### [HOLD]

Working material the author currently likes and may continue building around.

It is stable enough for iterative drafting, but still non-canonical. Do not use [HOLD] material as a continuity anchor, story-bible fact, or issue implementation requirement unless the user explicitly takes it off hold or asks to implement it.

### [CANON]

Explicitly approved continuity.

Canonical material may be committed to files, referenced by future scenes, added to story-bible material, and logged in issues as fixed continuity.

### Operational rule

Before any repo write action, including issue creation, file updates, pull requests, lore updates, and summaries that may become handoff material, verify what in the conversation is actually canonical. If unclear, generalise. Prefer emotional or structural abstractions over provisional nouns.

Do not invent proper nouns during implementation or profile/entity updates. If source prose or an issue says "the bear," "the corner shop," "the alley," "the paper," or another generic phrase, preserve that generic phrase unless the user explicitly approves a name. Naming a character, shop, street, institution, organisation, object, case, publication, or company is a canon decision, not a prose-smoothing convenience.

## Working rule

For any task:

1. Read `README.md`.
2. Load the story bible, prompt pack, and narration rules.
3. Load only task-relevant drafts, chapters, scenes, outlines, or notes.
4. Keep canonical prose, scene studies, outlines, and notes in their appropriate folders.
5. Do not promote exploratory plot material into canon unless explicitly asked.
6. Apply the drafting-state protocol before repo writes or issue logging.
7. For writing work, retrieve and summarize scope-specific context before generating prose.
8. For extraction or profile-scan work, prefer validated issue logging over direct canon edits unless the user explicitly asks to apply the change now.
9. For review, profile-scan, extraction, scaffold-capture, or writing-follow-up logging work, check for already-open matching issues before creating a new one.
10. When a session or prose scan introduces durable case, object, organisation, or character information, decide whether it belongs in an existing entity surface or whether a new candidate issue is needed to establish that surface cleanly.
11. When files or folders are added, removed, moved, or renamed, refresh the generated repo manifest and update the relevant README or file index in the same change.

When a durable surface is needed for an unnamed entity, use a generic bounded description in the profile name and file path. Do not create an in-world name to make the surface feel complete.

For ordinary writing connection, keep the user-facing summary compact. Include the active draft/scene, a short cue from the last saved prose, and a direct question about what the author wants to write or change next. Do not dump the full context checklist unless the author asks or a canon/provisional decision is needed.

## Review Path

Use this path when the user asks for review, critique, assessment, audit, feedback, or whether a passage "works".

Review work is read-only unless the user explicitly asks for implementation after the review.

The reviewer's job is to compare the requested material against the repo's established rules and story logic, then log detailed issues. Do not rewrite, patch, or resolve the issues during review mode.

Before reviewing, load:

1. `README.md`
2. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
3. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
4. `rules/noir_narration_rules.md`
5. relevant character profiles
6. relevant location profiles
7. Any relevant chapter, scene, outline, or note named by the user
8. `../ElectricMonk/notes/mode_preflight_workflow.md` when issue logging or dedupe is likely

Review priorities, in order:

1. Pacing and feel of the prose.
2. Match to Dragon's first-person noir voice.
3. Tone consistency across the passage or requested scope.
4. Consequence-first narration rather than flat stage directions.
5. Implication-heavy emotional movement rather than direct explanation.
6. Toy-world play-as-reality logic.
7. Character consistency, motives, and action logic, especially Dragon and the pink dragon, against the current character files.
8. Location consistency and stable spatial logic against the current location files.
9. Canon/provisional boundary discipline.
10. Factual continuity within the current draft.
11. Scene function and structural flow.

When logging an issue, include:

- location or quoted short phrase
- severity or priority
- what rule, canon point, or style principle it conflicts with
- why it affects pacing, feel, logic, character, or continuity
- one or more suggested directions for resolving it

If review identifies a conflict or uncertainty that needs author input before the issue can be framed correctly:

1. ask one clarification question at a time
2. let the author correct the diagnosis
3. restate the issue in corrected form
4. then log it

The default repair path in review mode is to identify and log issues, not to fix them directly.

Before logging a new review or consistency-fix issue, check whether an open issue already tracks the same clash or gap.

Do not treat personal preference as an issue unless it affects the established noir voice, pacing, canon, or story logic.

Do not flatten the review into general praise. If no issues are found, say so clearly and mention any residual risk or area worth watching.

## Issue Workflow Path

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

If the user asks to "log a ticket", "log an issue", "create an issue", or "make a ticket", create a GitHub issue using this repo's issue templates and the Monk rules in `../ElectricMonk/notes/issue_workflow.md`; do not edit repository files unless the user separately asks for implementation.

When the user asks to process, resolve, implement, or close GitHub issues:

1. Load `../ElectricMonk/notes/issue_workflow.md`.
2. Identify the issue type: implementation, review, planning/scaffold, or canon promotion.
3. Treat the issue as scoped instructions.
4. Enter the `Implementation Wizard` from `../ElectricMonk/notes/issue_workflow.md` before making any change.
5. Present concrete proposed changes one by one and get approval before each edit.
6. Apply the acceptance criteria from `../ElectricMonk/notes/issue_workflow.md` before closing the issue.
7. Run the post-implementation style/flow conflict check from `../ElectricMonk/notes/issue_workflow.md` when the issue changes prose, style guidance, narration rules, character guidance, or scene structure.
8. If the scoped work is complete but an acceptance criterion or style/flow check reveals an out-of-scope problem, create a follow-up issue that explains the problem instead of broadening the current issue.

Do not use an issue as permission to broadly rewrite unrelated prose, promote provisional material, or clean up surrounding structure unless the issue explicitly asks for it.

Do not use an issue as permission to name unnamed entities. If naming is not part of the issue, keep unnamed figures, shops, institutions, objects, publications, and companies generic.

When the user asks to log or create a GitHub issue, use the appropriate template from this repo's `.github/ISSUE_TEMPLATE/` directory and the Monk rules in `../ElectricMonk/notes/issue_workflow.md`.

## README / Path Index Maintenance

When adding, removing, renaming, or moving any file or folder, update the relevant README or file index in the same change.

Keep the root `README.md` current.

When adding, removing, renaming, or changing the status of a major chapter, scene, outline, or planning artifact, update the root README's Chapter Status table in the same change.

For top-level project structure changes, update the root `README.md` and/or this file as appropriate.
