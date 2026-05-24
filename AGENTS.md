# Agent Instructions

Before working in this repository, read:

1. `../ElectricMonk/AGENTS.md`
2. `README.md`
3. `AI_REPO_CONTEXT.md`

Use `../ElectricMonk/` for Monk workflow machinery. Use this repository for Toy Noir Dragon story content, canon, style, prose, and project-specific issue scope.

Follow the scope, canon, and provisional-material rules in this repository's files.

This repository is dedicated to the Toy Noir Dragon continuity. Do not add or recreate family Dragon project material unless the user explicitly asks for comparison, adaptation, or crossover and provides the needed source context.

## Connector / Limited-Access Fallback

If an agent enters this repository through a connector or chat interface that cannot read the sibling `../ElectricMonk/` repository, it must say so explicitly before continuing. It may still orient to this repository, but it must use the local fallback rules in `AI_REPO_CONTEXT.md` and must not claim that the full Monk workflow is loaded.

For writing, drafting, continuation, or prose revision, do not generate prose until these local files have been read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
4. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
5. `rules/noir_narration_rules.md`
6. `characters/dragon_character_profile.md`
7. The active chapter, scene, outline, location, case, object, or organisation files relevant to the requested passage

Writing-mode hard stops:

- Dragon narration is first-person past tense unless the user explicitly asks for another form.
- Before continuing prose, identify the current saved endpoint from the active draft or clearly mark any chat-only forward material as `[HOLD]` / not yet canon.
- Do not treat issue summaries, remembered beats, or references to unavailable transcripts as prose. If the actual forward prose is not visible, say so, compare against the saved draft, and ask for the source text before reconstructing, logging, or integrating it.
- For prose implementation, distinguish exact agreed prose from beat summaries. If an issue or chat only lists beats, implement only by explicit reconstruction approval; otherwise ask for the exact prose instead of filling gaps.
- Do not treat pasted prose in a diagnostic, review, complaint, or "what went wrong" conversation as approved source prose. It is evidence until the user explicitly says to use that exact wording.
- When the author asks to replace, continue, revise, or draft a passage, satisfy that prose request before pivoting into craft analysis, design questions, or issue logging. Do not convert a concrete prose instruction into abstract style findings unless the author explicitly asks for analysis or capture.
- If the active endpoint, narrator, or relevant local style/canon files cannot be confirmed, ask for clarification instead of drafting from general noir vibes.

## Review Path

When the user asks for review, critique, assessment, audit, or feedback, follow the Review Path in `AI_REPO_CONTEXT.md`.

In review work, do not edit story files or resolve the issues yourself unless the user separately asks for implementation. Only report detailed issues, explain why each issue conflicts with the repo rules or story logic, and suggest possible fixes.

## Issue Workflow

When the user asks to process, resolve, implement, or close GitHub issues, load `../ElectricMonk/notes/issue_workflow.md` and follow its issue-type rules and acceptance criteria, plus the Toy Noir Dragon project-specific rules in `AI_REPO_CONTEXT.md`.

Treat issues as scoped handoff instructions. Do not broaden the task, promote provisional material, or rewrite unrelated prose unless the issue explicitly asks for it.

Do not invent proper nouns while implementing scoped issues. New names for characters, shops, streets, institutions, organisations, objects, cases, publications, or companies require explicit user approval or issue scope. Preserve generic descriptions when the source uses them.

If the scoped work is complete but acceptance criteria or the post-implementation style/flow check expose a real out-of-scope problem, allow the implementation through and create a follow-up issue explaining what is wrong, where it appears, and suggested resolution directions.

When logging a new issue, use the appropriate template from this repo's `.github/ISSUE_TEMPLATE/` directory and the Monk issue rules in `../ElectricMonk/notes/issue_workflow.md`.

If the user asks to "log a ticket", "log an issue", "create an issue", or "make a ticket", create a GitHub issue using the appropriate template and do not edit repository files unless the user separately asks for implementation.

## README / Path Index Maintenance

When adding, removing, renaming, or moving any file or folder, update the relevant README or file index in the same change.

For project files, keep the root `README.md` current.

When adding, removing, renaming, or changing the status of a major chapter, scene, outline, or planning artifact, update the root README's Chapter Status table in the same change.

For top-level project structure changes, update the root `README.md` and/or `AI_REPO_CONTEXT.md` as appropriate.
