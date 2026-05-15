# AI Repo Context — Dragon Noir

This repository contains only the standalone Toy Noir Dragon book project.

The family Dragon project is no longer part of this repository. It remains in the old `Dragon-Stories` repository history and should not be used as guidance here unless the user explicitly provides or requests it for comparison, adaptation, or crossover.

## First file to read

Always read `README.md` first.

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

## Context loading

For Toy Noir Dragon work, load:

1. `README.md`
2. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
3. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
4. `rules/noir_narration_rules.md`
5. Relevant character profiles under `characters/`
6. Relevant files under:
   - `chapters/`
   - `scenes/`
   - `outlines/`
   - `notes/`

For GitHub issue work, also load `notes/issue_workflow.md`.

For repo-entry and mode-routing work, also load `notes/repo_connection_workflow.md`.

For drafting or prose-revision work, also load `notes/writing_workflow.md`.

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

## Working rule

For any task:

1. Read `README.md`.
2. Load the story bible, prompt pack, and narration rules.
3. Load only task-relevant drafts, chapters, scenes, outlines, or notes.
4. Keep canonical prose, scene studies, outlines, and notes in their appropriate folders.
5. Do not promote exploratory plot material into canon unless explicitly asked.
6. Apply the drafting-state protocol before repo writes or issue logging.
7. For writing work, retrieve and summarize scope-specific context before generating prose.

## Review Path

Use this path when the user asks for review, critique, assessment, audit, feedback, or whether a passage "works".

Review work is read-only unless the user explicitly asks for implementation after the review.

The reviewer's job is to compare the requested material against the repo's established rules and story logic, then log detailed issues. Do not rewrite, patch, or resolve the issues during review mode.

Before reviewing, load:

1. `README.md`
2. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
3. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
4. `rules/noir_narration_rules.md`
5. `characters/pink_dragon_character_profile.md` when the pink dragon is relevant
6. Any relevant chapter, scene, outline, or note named by the user

Review priorities, in order:

1. Pacing and feel of the prose.
2. Match to Dragon's first-person noir voice.
3. Consequence-first narration rather than flat stage directions.
4. Implication-heavy emotional movement rather than direct explanation.
5. Toy-world play-as-reality logic.
6. Character consistency, especially Dragon and the pink dragon.
7. Canon/provisional boundary discipline.
8. Factual continuity within the current draft.
9. Scene function and structural flow.

When logging an issue, include:

- location or quoted short phrase
- severity or priority
- what rule, canon point, or style principle it conflicts with
- why it affects pacing, feel, logic, character, or continuity
- one or more suggested directions for resolving it

Do not treat personal preference as an issue unless it affects the established noir voice, pacing, canon, or story logic.

Do not flatten the review into general praise. If no issues are found, say so clearly and mention any residual risk or area worth watching.

## Issue Workflow Path

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

If the user asks to "log a ticket", "log an issue", "create an issue", or "make a ticket", create a GitHub issue using the appropriate template from `notes/issue_workflow.md` and do not edit repository files unless the user separately asks for implementation.

When the user asks to process, resolve, implement, or close GitHub issues:

1. Load `notes/issue_workflow.md`.
2. Identify the issue type: implementation, review, planning/scaffold, or canon promotion.
3. Treat the issue as scoped instructions.
4. Apply the acceptance criteria from `notes/issue_workflow.md` before closing the issue.
5. Run the post-implementation style/flow conflict check from `notes/issue_workflow.md` when the issue changes prose, style guidance, narration rules, character guidance, or scene structure.
6. If the scoped work is complete but an acceptance criterion or style/flow check reveals an out-of-scope problem, create a follow-up issue that explains the problem instead of broadening the current issue.

Do not use an issue as permission to broadly rewrite unrelated prose, promote provisional material, or clean up surrounding structure unless the issue explicitly asks for it.

When the user asks to log or create a GitHub issue, use the appropriate template from `notes/issue_workflow.md`.

## README / Path Index Maintenance

When adding, removing, renaming, or moving any file or folder, update the relevant README or file index in the same change.

Keep the root `README.md` current.

When adding, removing, renaming, or changing the status of a major chapter, scene, outline, or planning artifact, update the root README's Chapter Status table in the same change.

For top-level project structure changes, update the root `README.md` and/or this file as appropriate.
