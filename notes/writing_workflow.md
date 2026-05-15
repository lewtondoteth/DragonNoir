# Writing Workflow

Provisional workflow for drafting, revising, or continuing prose in the Dragon Noir repository.

This workflow exists to force retrieval before generation. The agent should not begin prose work from general vibe alone. It should first identify the scope of the work, load the relevant local guidance, and summarize what already governs that scope.

It also exists to prevent unapproved scaffold, style, character-guidance, or location-guidance material from quietly steering the prose. If relevant scaffold, local-pattern, style-guidance, provisional character-profile items, provisional location-profile items, or held global-rule candidates are present but not yet approved for drafting use, the agent must surface them and pause for approval before writing.

## Purpose

Use this workflow when the author wants:

- drafting
- chapter continuation
- scene revision
- prose integration
- structural prose editing
- chapter-specific implementation work

The core rule is:

> Before writing, ask what already exists for this scope.

## Retrieval Before Generation

Before drafting any prose, the agent must identify the target scope.

Possible scopes include:

- chapter
- scene
- character dynamic
- case/object sequence
- general prose work

Then the agent must load the relevant files in a strict order.

## Retrieval Order

### 1. Global Guidance

Always load:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/mode_preflight_workflow.md`
4. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
5. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
6. `rules/noir_narration_rules.md`

Refresh `notes/repo_manifest.json` with `python3 tools/generate_repo_manifest.py` when the tree has changed or the scope is non-trivial.

### 2. Scope-Specific Canon

Load the active canonical file for the scope, if one exists.

Examples:

- chapter draft in `chapters/`
- active character profile in `characters/`
- active location profile in `locations/`
- relevant canon note if explicitly marked active

### 3. Scope-Specific Structure

Load the governing outline or structural reference.

Examples:

- `outlines/chapter_01_narrative_beats.md`
- chapter-specific planning note
- sequence scaffold if explicitly relevant

### 4. Scope-Specific Local Guidance

Load the bounded files that may contain approved local patterns or active working constraints.

Examples:

- chapter-specific notes
- relevant scene studies
- relevant character files
- relevant location files
- approved chapter-level pattern notes

### 5. Provisional / Experimental Material

Load only if it is explicitly relevant to the requested work.

Do not let exploratory material override active canon.

## Pre-Writing Approval Check

After retrieval and before drafting, the agent must check whether any relevant scaffold or style items still need approval for use in this writing pass.

This includes:

- held `Global Rule` candidates that would materially shape the current writing pass
- scaffolds that shape the chapter, scene, reveal order, case movement, or acceptance logic
- local patterns that materially affect how the scene should function
- style guidance that would change pacing, implication, recognition logic, or narration behavior for this scope
- character-profile items, dynamic notes, or profile-change candidates that would materially shape behavior, reaction, presentation, or relationship logic in this draft
- location-profile items or location-guidance candidates that would materially shape atmosphere, place logic, civic pressure, layout, or recurring scene function in this draft

The agent should distinguish between:

- already approved for drafting use
- present in the repo but still `[EXPLORE]` or `[HOLD]`
- ambiguous enough that approval is still needed

If a global-rule candidate, scaffold, style, or character-guidance item would materially steer the prose and is not already approved for drafting use, the agent must pause and run a one-by-one approval check before writing.

## Open-Issue Check Before Approval

Before presenting an approval card for a non-canon item, check whether an open GitHub issue already exists for that exact guidance or scaffold.

If an open issue already exists:

- mention it in the summary or card
- do not promise to log a second issue for the same thing
- let the author approve the item for the current writing pass without treating that approval as new canon

If no open issue exists and the item is approved for use in the writing pass:

- the default follow-up should be to preserve it through the appropriate issue-handoff path after drafting, unless the author explicitly says not to log it
- use the existing issue categories from `notes/issue_workflow.md`

This prevents duplicate issues and also prevents draft-shaping approvals from vanishing without a paper trail.

## Approval Card Format

When approval is needed, present each item one by one using a short validation card.

Each card should state:

- `Type`: `Scaffold`, `Local Pattern`, `Style Guidance`, `Character Profile Item`, `Dynamic Guidance`, `Profile Change Candidate`, or `Location Profile Item`
- `Scope`: `Global`, `Chapter`, `Scene`, or `Dynamic`
- `Current State`: `[EXPLORE]`, `[HOLD]`, or already approved
- `Summary`: what the item says in plain language
- `Proposed Use In Drafting`: how it would affect this writing pass
- `Suggested Source`: where the item currently lives
- `Existing Open Issue`: issue number/link if one already exists, otherwise `none found`

The author should be able to answer in plain language, for example:

- `yes`
- `yes that's right`
- `no`
- `hold`
- `correct: ...`

If the author corrects the explanation, the agent should restate its understanding before treating the item as approved for use.

If the author approves an item in this step, it may guide the current writing pass. That does not automatically make it global canon.

In Writing mode, approval means:

- approved for this writing pass
- not automatically canon
- preserve or reference the relevant issue handoff unless the item is already adequately tracked or the author explicitly declines logging

## Logging Path For Drafting Guidance

If the author wants a validated item preserved without immediately updating canon files, use the issue-handoff path from `notes/issue_workflow.md`.

This applies to:

- scaffold items worth preserving as future work
- style or local-pattern guidance not yet ready for direct canon edits
- character-profile or dynamic guidance not yet ready for profile updates
- location-profile guidance not yet ready for direct profile updates

In this logging path:

- approval still happens one item at a time
- before logging, check whether an open issue already exists for the same item
- `yes that's right` may be treated as approval to log immediately when the author has made logging the active path
- the resulting issue preserves the approved item without treating it as already canon
- if an open issue already exists, do not create a duplicate; reference the existing issue and continue drafting
- later implementation must repeat the relevant manual check before updating character profile, location profile, rule, bible, or note files

When Writing mode triggered the approval card, the default interpretation should be:

> approve for this draft now, and make sure the repo has the right follow-up issue unless one already exists

## Required Pre-Draft Summary

Before generating prose, the agent should summarize what it found for the requested scope.

The summary should usually include:

- active canon file for this scope
- governing outline or structure file
- relevant local patterns or chapter-level constraints
- relevant approved global rules and any held global-rule candidates that may need review
- relevant scaffolds or style items already approved for drafting use
- any scaffold, style, or character-guidance items that still require approval before drafting
- relevant character, dynamic, or location constraints
- any already-open issues that are likely to matter to this writing pass
- what not to import or over-promote

The goal is to be able to say:

> We are working on Chapter 1. Here is the active draft, the governing outline, the relevant local constraints, and the things we should not accidentally import.

## Chapter Workflow

If the work is chapter-based, the agent should explicitly answer:

1. What is the active canonical chapter file?
2. What outline governs this chapter?
3. What scene studies or chapter notes are relevant?
4. What local patterns have been approved for this chapter, if any?
5. What held global-rule candidates might materially affect this chapter and still need review?
6. What relevant scaffolds, style items, or location-profile items still need approval before they can shape the prose?
7. What open issues already track those items, if any?
8. What provisional material is nearby but should not be mistaken for canon?

Example for Chapter 1:

- active draft: `chapters/chapter_01_opening.md`
- active outline: `outlines/chapter_01_narrative_beats.md`
- relevant scene study: `scenes/chapter_01_office_entry_coffee_ritual_draft.md`
- relevant notes: opening-case scaffold only if explicitly needed

## Scene Workflow

If the work is scene-based, the agent should explicitly answer:

1. What chapter does this scene belong to?
2. What canonical chapter material surrounds it?
3. What local scene study or draft already exists?
4. What chapter-level patterns constrain this scene?
5. What held global-rule candidates would materially shape this scene?
6. What scaffolds or style items would materially shape this scene?
7. Which of those are approved for drafting use, and which still need approval?
8. What open issues already track those items, if any?
9. What character-dynamic rules matter here?

## Character Workflow

If the work is character-focused, the agent should explicitly answer:

1. What character profile is authoritative?
2. What story-bible material governs the character?
3. What local chapter or scene constraints affect this appearance?
4. What profile items, dynamic notes, patterns, or style items belong only to this dynamic rather than the whole project?
5. Which of those are already approved for drafting use?
6. Which held global-rule candidates are relevant here and still need review?
7. Which still need one-by-one approval before they shape the prose?
8. What open issues already track those items, if any?

## Local Pattern Retrieval

When local patterns have been validated and stored, the agent should prefer them for the relevant scope before falling back to global rules.

Priority order:

1. active canon for the requested scope
2. approved local patterns for that scope
3. approved scaffold items for that scope
4. global narration and story rules
5. exploratory nearby material only if explicitly requested

The agent should not flatten a local pattern into a global law while drafting.

Unapproved scaffold, style, or character-guidance items may be discussed, summarized, or offered for approval, but they should not quietly govern the draft.

Held global-rule candidates should also be surfaced when they are relevant. They do not automatically block writing, but they should not quietly become de facto canon through repeated drafting use without review.

## Pre-Draft Questions The Agent Must Answer Internally

Before writing, the agent should be able to answer:

- What scope am I writing in?
- What is the active canon file for this scope?
- What outline or structure governs it?
- What local patterns or constraints apply here?
- What held global-rule candidates are relevant to this scope?
- What relevant scaffold or style items are already approved for drafting use?
- What relevant character-profile or dynamic-guidance items are already approved for drafting use?
- What scaffold, style, or character-guidance items still require approval?
- What open issues already track those items?
- What material is nearby but should not be promoted?

If the agent cannot answer those questions, it should load more context before drafting.

## What Writing Mode Should Not Do

Do not:

- draft from the story bible alone when a local chapter file exists
- ignore the chapter outline
- treat experimental scene files as canon by default
- import provisional plot details without explicit permission
- let `[EXPLORE]` or `[HOLD]` scaffold/style/character-guidance material silently steer the prose
- let `[HOLD]` global-rule candidates quietly become default canon through use
- apply global rules while forgetting scope-specific local patterns
- ignore an existing open issue and prompt or log as if the item were untracked
- skip the one-by-one approval step when unapproved scaffold, style, or character-guidance items matter to the draft
- start prose generation before summarizing what governs the requested scope

## Minimal Agent Prompt

Use this when asking an agent to do writing work:

```text
Connect to my repo lewtondoteth/DragonNoir and switch to Writing mode.

Before drafting, follow `notes/writing_workflow.md`.

Identify the scope of the work, load the active canon file, the governing outline, the relevant local notes/scenes/character files, and summarize what already governs this scope. Then continue with the prose work.

If any relevant scaffold, style, or character-guidance items are not yet approved for drafting use, pause and run the one-by-one approval check before writing.

Before prompting any approval card for a non-canon item, check whether an open issue already tracks it. If the item is approved for this writing pass and no issue exists, preserve it through the correct issue-handoff path after drafting unless I explicitly say not to log it.
```
