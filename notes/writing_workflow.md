# Writing Workflow

Provisional workflow for drafting, revising, or continuing prose in the Dragon Noir repository.

This workflow exists to force retrieval before generation. The agent should not begin prose work from general vibe alone. It should first identify the scope of the work, load the relevant local guidance, and summarize what already governs that scope.

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
3. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
4. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
5. `rules/noir_narration_rules.md`

### 2. Scope-Specific Canon

Load the active canonical file for the scope, if one exists.

Examples:

- chapter draft in `chapters/`
- active character profile in `characters/`
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
- approved chapter-level pattern notes

### 5. Provisional / Experimental Material

Load only if it is explicitly relevant to the requested work.

Do not let exploratory material override active canon.

## Required Pre-Draft Summary

Before generating prose, the agent should summarize what it found for the requested scope.

The summary should usually include:

- active canon file for this scope
- governing outline or structure file
- relevant local patterns or chapter-level constraints
- relevant character or dynamic constraints
- what not to import or over-promote

The goal is to be able to say:

> We are working on Chapter 1. Here is the active draft, the governing outline, the relevant local constraints, and the things we should not accidentally import.

## Chapter Workflow

If the work is chapter-based, the agent should explicitly answer:

1. What is the active canonical chapter file?
2. What outline governs this chapter?
3. What scene studies or chapter notes are relevant?
4. What local patterns have been approved for this chapter, if any?
5. What provisional material is nearby but should not be mistaken for canon?

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
5. What character-dynamic rules matter here?

## Character Workflow

If the work is character-focused, the agent should explicitly answer:

1. What character profile is authoritative?
2. What story-bible material governs the character?
3. What local chapter or scene constraints affect this appearance?
4. What patterns belong only to this dynamic rather than the whole project?

## Local Pattern Retrieval

When local patterns have been validated and stored, the agent should prefer them for the relevant scope before falling back to global rules.

Priority order:

1. active canon for the requested scope
2. approved local patterns for that scope
3. global narration and story rules
4. exploratory nearby material only if explicitly requested

The agent should not flatten a local pattern into a global law while drafting.

## Pre-Draft Questions The Agent Must Answer Internally

Before writing, the agent should be able to answer:

- What scope am I writing in?
- What is the active canon file for this scope?
- What outline or structure governs it?
- What local patterns or constraints apply here?
- What material is nearby but should not be promoted?

If the agent cannot answer those questions, it should load more context before drafting.

## What Writing Mode Should Not Do

Do not:

- draft from the story bible alone when a local chapter file exists
- ignore the chapter outline
- treat experimental scene files as canon by default
- import provisional plot details without explicit permission
- apply global rules while forgetting scope-specific local patterns
- start prose generation before summarizing what governs the requested scope

## Minimal Agent Prompt

Use this when asking an agent to do writing work:

```text
Connect to my repo lewtondoteth/DragonNoir and switch to Writing mode.

Before drafting, follow `notes/writing_workflow.md`.

Identify the scope of the work, load the active canon file, the governing outline, the relevant local notes/scenes/character files, and summarize what already governs this scope. Then continue with the prose work.
```
