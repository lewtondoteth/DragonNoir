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
├── notes/
│   ├── README.md
│   ├── development_options.md
│   ├── issue_workflow.md
│   └── opening_case_music_box_scaffold.md
├── outlines/
│   └── chapter_01_narrative_beats.md
├── rules/
│   └── noir_narration_rules.md
├── scenes/
│   ├── README.md
│   └── chapter_01_office_entry_coffee_ritual_draft.md
└── story_bible/
    ├── README.md
    ├── Toy_Noir_Dragon_AI_Prompt_Pack.md
    └── Toy_Noir_Dragon_Standalone_Story_Bible.md
```

## Working Structure

- `chapters/` — canonical or assembled chapter drafts
- `scenes/` — scene drafts, fragments, and scene-level experiments
- `outlines/` — chapter architecture, narrative beats, and pacing references
- `characters/` — canonical character profiles and expanded continuity notes
- `rules/` — canonical practical writing rules discovered during drafting
- `discarded_or_experimental/` — retired alternatives and preserved non-canonical material
- `notes/` — planning notes, continuity tracking, mystery structure, and revision notes
- `story_bible/` — authoritative noir project bible and prompt pack

## Chapter 1 Workflow

- Canonical current draft: `chapters/chapter_01_opening.md`
- Canonical pacing reference: `outlines/chapter_01_narrative_beats.md`
- Current experimental scene sandbox: `scenes/chapter_01_office_entry_coffee_ritual_draft.md`
- Practical narration rules: `rules/noir_narration_rules.md`
- Opening-case scaffold: `notes/opening_case_music_box_scaffold.md`
- Issue workflow: `notes/issue_workflow.md`

Keep canonical prose, experimental scene drafts, and structural outlines separate while drafting.

## Current Active Drafts

- `chapters/chapter_01_opening.md` — canonical current Chapter 1 draft. Contains the rain/city opening, Dragon's trifle-hangover state, doorway reveal, office-entry transition, coffee sequence, and layered recognition progression.

## Scene Studies

- `scenes/chapter_01_office_entry_coffee_ritual_draft.md` — experimental office-entry and coffee material. Retained as a scene-study sandbox; do not treat as canonical prose unless integrated into `chapters/chapter_01_opening.md`.

## Outlines And Notes

- `outlines/chapter_01_narrative_beats.md` — canonical Chapter 1 pacing and architecture reference.
- `notes/issue_workflow.md` — GitHub issue handoff workflow, issue types, and acceptance criteria.
- `notes/opening_case_music_box_scaffold.md` — exploratory stolen music box opening-case scaffold. Not fixed canon.
- `notes/development_options.md` — retired, backup, and exploratory ideas. Not active canon unless explicitly revived.

## Issue Workflow

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

Issue workflow reference:

- `notes/issue_workflow.md`

Implementation agents should treat issues as scoped instructions, not permission to broadly rewrite. Review issues use the read-only AI Review Path. Planning/scaffold issues stay provisional unless the issue explicitly says to promote material into canon.

When logging a new issue, use the templates in `notes/issue_workflow.md` for implementation, review, planning/scaffold, canon promotion, and follow-up issues.

Before closing an implementation issue, check the acceptance criteria in `notes/issue_workflow.md`, including scope control, canon/provisional boundaries, README/path updates, prose style, character continuity, and `git diff --check`.

If the scoped work is complete but a criterion exposes a real out-of-scope problem, the agent should allow the implementation through and create a follow-up issue explaining what is wrong and how it might be resolved.

## Canonical vs Experimental

- Canonical: story bible, narration rules, character profiles, active chapter drafts, and active outline references.
- Development: notes and opening-case scaffolds that preserve possibilities without locking plot.
- Experimental: scene sandboxes and pacing studies.
- Retired: discarded or backup ideas preserved for later comparison or revival.

## AI Review Path

When asking an AI agent to review, critique, assess, audit, or give feedback, the agent should use a read-only review path.

Review mode means:

- do not edit story files
- do not resolve issues directly
- compare the requested material against the story bible, prompt pack, narration rules, character profiles, and relevant outlines/notes
- log detailed issues with reasons and suggested resolution directions

Review should focus especially on:

- pacing and feel of the prose
- whether the passage matches Dragon's first-person noir voice
- consequence-first narration instead of flat stage directions
- implication-heavy emotional movement
- toy-world play-as-reality logic
- character consistency
- canon/provisional boundaries
- factual continuity inside the draft
- scene function and structural flow

An issue report should explain where the problem appears, why it conflicts with the repo's rules or story logic, how it affects pacing/feel/continuity/character, and what kind of revision would resolve it.

Agents should not rewrite the passage during review unless the user explicitly asks for implementation after the review.

## Active Canon

The active canon is Dragon, the pink dragon, Toy City, narration style, repair logic, treasure instinct, rain logic, play-as-reality toy ontology, and the emotional/thematic dynamics between the two dragons.

The exact case, mystery engine, artifact, antagonist, and ending structure are provisional until deliberately promoted into the story bible.

Retired/provisional noir plot material, including the Ember-Stone, Patchwork Guardian, wind-up mouse courier, and related fixed-plot machinery, belongs in development notes and should not be treated as active canon unless explicitly revived.
