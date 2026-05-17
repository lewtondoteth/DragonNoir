# Writing Workflow

Provisional workflow for drafting, revising, or continuing prose in the Dragon Noir repository.

This workflow exists to force retrieval before generation. The agent should not begin prose work from general vibe alone. It should first identify the scope of the work, load the relevant local guidance, and summarize what already governs that scope.

It also exists to prevent unapproved scaffold, style, character-guidance, or location-guidance material from quietly steering the prose. If relevant scaffold, local-pattern, style-guidance, provisional character-profile items, provisional location-profile items, or held global-rule candidates are present but not yet approved for drafting use, the agent must surface them and pause for approval before writing.

One exception exists for author-supplied prose progress that is already captured in open writing/prose issues. Writing mode may use that material as provisional forward-draft context so the author can keep writing from where the exploratory work has reached before the issue implementation process catches up. This does not make the issue material canon and does not replace later issue processing.

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

The second working rule is:

> When the author's taste flags a line as wrong, help name why before trying to preserve the lesson.

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
- active case profile in `cases/`
- active object profile in `objects/`
- active organisation profile in `organisations/`
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
- relevant case files
- relevant object files
- relevant organisation files
- approved chapter-level pattern notes

### 5. Provisional / Experimental Material

Load only if it is explicitly relevant to the requested work.

Do not let exploratory material override active canon.

### 6. Forward Draft Context From Open Prose Issues

When the author wants to keep writing and the repo may lag behind their latest approved-in-chat prose, check for open GitHub issues that preserve writing progress for the requested scope before asking for approval cards.

Look for open issues that contain or clearly reference:

- prose to preserve
- chapter continuation material
- scene replacement or extension text
- accepted drafting-session output not yet implemented
- long-session capture items whose prose portion is explicitly intended as forward draft context
- chapter-specific prose issues for the active chapter or scene

If such issues exist, the agent should build a temporary internal `Forward Draft Context`:

1. identify the active canon endpoint from the repo file
2. identify the latest issue-tracked prose or scene movement beyond that endpoint
3. summarize only the minimum forward state needed to continue writing
4. mark that state as `[HOLD]` / issue-tracked / not yet canon
5. track which issue or source each forward-context item came from
6. use it to understand where the author is currently writing from

This step lets writing continue from the author's real current draft position without forcing the author to process every implementation issue first.

Do not paste the whole issue content into chat unless the author asks. The normal startup can simply say that issue-tracked forward context was found and is being used provisionally.

Forward Draft Context may guide the current writing pass without a separate approval card only when:

- it comes from an open issue or author-provided prose source for the same chapter/scene
- it is being used to continue drafting, not to update canon files
- the agent keeps the repo's canon/provisional boundary explicit
- later implementation will still process the issue normally before writing to canon files

If the issue contains new rules, profile changes, lore, case facts, or broad style guidance beyond prose continuity, those still follow the normal approval and validation paths before they can become durable guidance.

Forward Draft Context is also the baseline for later writing-session logging. If the author asks to log follow-up material after drafting from forward context, log only the new delta beyond:

- the saved canon file
- the issue-tracked forward context already loaded
- existing open issues for the same prose, scene movement, rule, profile item, or scaffold
- existing repo guidance that already captures the point

Do not re-log all loaded issue material just because it was used for drafting continuity.

## Taste Diagnosis During Drafting

During live prose work, the author may know that a line, beat, or paragraph is wrong before they can explain why.

Treat comments like these as useful style signals:

- `the shape is wrong`
- `this doesn't sit right`
- `the rhythm is off`
- `too neat`
- `too pretty`
- `too direct`
- `not Dragon`
- `wrong kind of sentence`
- `it skipped a step`
- `closer, but still wrong`

The agent should not demand that the author justify the reaction before continuing. Instead, it should help diagnose the problem.

Recommended response:

1. offer two or three compact possible diagnoses
2. tie each diagnosis to a concrete prose feature, such as pace, directness, sentence polish, Dragon's voice, object detail, emotional explanation, joke timing, or skipped physical consequence
3. offer a small replacement or revision direction
4. let the author confirm, reject, or correct the diagnosis in plain language

Example:

```text
Possible diagnosis:
1. It explains the feeling before the object detail carries it.
2. It sounds too polished for Dragon's tired practical voice.
3. It jumps to the reveal before the room has reacted.

I would try making the sentence plainer and putting the pressure on the catalogue/object first.
```

If the author confirms a diagnosis, treat the confirmed reason as extractable writing knowledge for later session extraction or follow-up logging.

When capturing the lesson later, preserve the reason rather than the exact rejected sentence unless the sentence itself is needed as evidence.

Useful capture shape:

- `Rejected / corrected feature`: what felt wrong
- `Confirmed reason`: why it failed, if discovered
- `Preferred direction`: what worked better
- `Scope`: global style rule, local Chapter 1 pattern, character/dynamic guidance, or scene-specific correction

If the author never finds a reason, preserve the reaction only lightly. Repeated similar reactions may become evidence for a later style pattern, but one unexplained dislike should not become a rule.

## Post-Logging Design-Choice Clarification

After logging or preserving writing-session material, the agent should briefly check whether the session contains design choices that would become more useful if the author explained them.

This is not a demand for more work. It is an optional follow-up offer.

Use this when the session includes:

- competing sentence options
- a chosen version and a rejected version
- a line or beat the author liked but did not explain
- a line or beat the author rejected as wrong, too direct, too pretty, too fast, not Dragon, or wrong shape
- pacing choices where one reveal order worked better than another
- humour choices where one joke landed and another did not
- character-response choices where one reaction felt more truthful

After logging the new material, the agent should say something like:

```text
I also spotted a few design choices in this session that could teach the repo more if you want to unpack them. We can go through them one by one: what the rejected option was doing wrong, why the chosen version works, and whether the lesson is global, local, or scene-specific.
```

If the author agrees, present one design-choice card at a time.

Each card should include:

- `Choice`: the decision point in plain language
- `Chosen Direction`: the version or approach the author preferred
- `Rejected Direction`: the alternative, if known
- `Likely Difference`: the agent's best short diagnosis
- `Question`: ask the author why the rejected option failed or why the chosen one worked

Do not log new guidance from these cards automatically. Treat the answers as fresh writing-session material that may later go through Session Extraction, rule validation, or issue logging.

After the author has unpacked one design choice, the agent should summarize the clarified lesson and offer to log that specific lesson as its own scoped follow-up.

Suggested wording:

```text
That gives us a clearer lesson: [one-sentence lesson]. Do you want me to log this specific design-choice note?
```

If the author says yes, log only the clarified design-choice delta, not the original prose or the whole previous session.

Before logging, classify the clarified lesson as one of:

- `Global Rule`
- `Local Pattern`
- `Character Guidance`
- `Location Guidance`
- `Case Guidance`
- `Object Guidance`
- `Organisation Guidance`
- `Scaffold Material`
- `Scene-Specific Correction`
- `Process Improvement`

Then check:

- whether the lesson is already captured in repo guidance
- whether an open issue already tracks the same lesson
- whether the lesson is reusable or just a scene-specific correction
- whether the author approved logging this specific clarified item

If it is already captured, say so and do not create a duplicate issue. If it is scene-specific, preserve it only if the author still wants it logged as a local implementation/revision note.

Keep the loop lightweight. If the author says they do not know why, offer two or three possible diagnoses and let them confirm, correct, or skip.

## Pre-Writing Approval Check

After retrieval and before drafting, the agent must check whether any relevant scaffold or style items still need approval for use in this writing pass.

This includes:

- held `Global Rule` candidates that would materially shape the current writing pass
- scaffolds that shape the chapter, scene, reveal order, case movement, or acceptance logic
- local patterns that materially affect how the scene should function
- style guidance that would change pacing, implication, recognition logic, or narration behavior for this scope
- character-profile items, dynamic notes, or profile-change candidates that would materially shape behavior, reaction, presentation, or relationship logic in this draft
- location-profile items or location-guidance candidates that would materially shape atmosphere, place logic, civic pressure, layout, or recurring scene function in this draft
- case-profile items or case-guidance candidates that would materially shape what the case appears to be, hides, or pressures in this draft
- object-profile items or object-guidance candidates that would materially shape object identity, value, function, or hidden pressure in this draft
- organisation-profile items or organisation-guidance candidates that would materially shape group pressure, cover story, or institutional behavior in this draft

The agent should distinguish between:

- already approved for drafting use
- present in the repo but still `[EXPLORE]` or `[HOLD]`
- ambiguous enough that approval is still needed

If a global-rule candidate, scaffold, style, or character-guidance item would materially steer the prose and is not already approved for drafting use, the agent must pause and run a one-by-one approval check before writing.

Do not treat issue-tracked forward prose context as a blocker in this step. Its job is to let the author continue writing before implementation catches up. Surface it as provisional context, use it for continuity during the writing session, and keep any broader guidance inside it subject to the normal approval rules.

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

- `Type`: `Scaffold`, `Local Pattern`, `Style Guidance`, `Character Profile Item`, `Dynamic Guidance`, `Profile Change Candidate`, `Location Profile Item`, `Case Profile Item`, `Object Profile Item`, or `Organisation Profile Item`
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
- case-profile guidance not yet ready for direct profile updates
- object-profile guidance not yet ready for direct profile updates
- organisation-profile guidance not yet ready for direct profile updates

In this logging path:

- approval still happens one item at a time
- before logging, check whether an open issue already exists for the same item
- compare against the current Forward Draft Context, if one was loaded
- log only the new material produced or clarified in the current writing session
- when creating a new issue, include a short `New Delta` note explaining what is new compared with the saved file and already-open issues
- `yes that's right` may be treated as approval to log immediately when the author has made logging the active path
- the resulting issue preserves the approved item without treating it as already canon
- if an open issue already exists, do not create a duplicate; reference the existing issue and continue drafting
- later implementation must repeat the relevant manual check before updating character profile, location profile, rule, bible, or note files

When Writing mode triggered the approval card, the default interpretation should be:

> approve for this draft now, and make sure the repo has the right follow-up issue unless one already exists

## Required Pre-Draft Context Check

Before generating prose, the agent should check what governs the requested scope.

Most of this check is internal. Do not dump the full checklist to the author unless they ask for it, the scope is ambiguous, or there is a canon/provisional risk that needs approval.

Internally, the agent should identify:

- active canon file for this scope
- any open prose/writing issues that move the author-facing draft beyond the active canon file
- the provisional forward-draft endpoint, if issue-tracked prose exists
- what content is already covered by those open issues and should not be logged again
- governing outline or structure file
- relevant local patterns or chapter-level constraints
- relevant approved global rules and any held global-rule candidates that may need review
- relevant scaffolds or style items already approved for drafting use
- any scaffold, style, or character-guidance items that still require approval before drafting
- relevant character, dynamic, or location constraints
- relevant case, object, or organisation constraints
- any already-open issues that are likely to matter to this writing pass
- what not to import or over-promote

## User-Facing Writing Startup

For ordinary writing continuation, the user-facing startup should be brief and focused.

It should usually include:

- `Scope`: the active chapter/scene/file being used
- `Last saved prose`: one short paraphrase or a very short quote from the end of the active draft
- `Forward context`: a short note only if open prose issues move the writing beyond the saved file
- `Next`: one simple question asking what the author wants to write, continue, or change

Keep this to roughly 3-6 short lines.

Example:

```text
I have Chapter 1 loaded.
Last saved prose: Odette has just drawn out a dry folded newspaper clipping and says, "Yesterday morning, I saw this."
The current guidance keeps this as intimate office noir before the auction-house case opens out.
What do you want to do next: continue from the clipping, revise the exchange before it, or try a new beat?
```

If the author asks for a detailed context recap, then provide the fuller governing-context summary.

The goal is to be able to proceed from:

> We are working on Chapter 1. Here is the active draft, the governing outline, the relevant local constraints, and the things we should not accidentally import.

without saying all of that every time.

## Chapter Workflow

If the work is chapter-based, the agent should answer these internally:

1. What is the active canonical chapter file?
2. What outline governs this chapter?
3. What scene studies or chapter notes are relevant?
4. Are there open prose/writing issues that contain author-facing chapter progress beyond the saved canon file?
5. If yes, what is the provisional forward-draft endpoint, and what must remain issue-tracked rather than canon?
6. What local patterns have been approved for this chapter, if any?
7. What held global-rule candidates might materially affect this chapter and still need review?
8. What relevant scaffolds, style items, or location-profile items still need approval before they can shape the prose?
9. What open issues already track those items, if any?
10. What provisional material is nearby but should not be mistaken for canon?

Example for Chapter 1:

- active draft: `chapters/chapter_01_opening.md`
- active outline: `outlines/chapter_01_narrative_beats.md`
- relevant scene study: `scenes/chapter_01_office_entry_coffee_ritual_draft.md`
- relevant notes: opening-case scaffold only if explicitly needed

## Scene Workflow

If the work is scene-based, the agent should answer these internally:

1. What chapter does this scene belong to?
2. What canonical chapter material surrounds it?
3. What local scene study or draft already exists?
4. Are there open prose/writing issues that contain scene progress beyond the saved canon file?
5. If yes, what is the provisional forward-draft endpoint, and what must remain issue-tracked rather than canon?
6. What chapter-level patterns constrain this scene?
7. What held global-rule candidates would materially shape this scene?
8. What scaffolds or style items would materially shape this scene?
9. Which of those are approved for drafting use, and which still need approval?
10. What open issues already track those items, if any?
11. What character-dynamic rules matter here?

## Character Workflow

If the work is character-focused, the agent should answer these internally:

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
- Is there issue-tracked prose that moves the author-facing draft beyond the active canon file?
- If yes, what is the provisional forward-draft endpoint, and what is still not canon?
- What is already covered by the saved file or open issues, so it should not be re-logged later?
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
- ignore issue-tracked prose progress and force the author to write from an artificially stale saved file
- treat experimental scene files as canon by default
- treat Forward Draft Context as canon or write it into repo files without normal issue processing
- log already-loaded Forward Draft Context as if it were new writing-session output
- import provisional plot details without explicit permission
- let `[EXPLORE]` or `[HOLD]` scaffold/style/character-guidance material silently steer the prose
- let `[HOLD]` global-rule candidates quietly become default canon through use
- apply global rules while forgetting scope-specific local patterns
- ignore an existing open issue and prompt or log as if the item were untracked
- skip the one-by-one approval step when unapproved scaffold, style, or character-guidance items matter to the draft
- start prose generation before checking what governs the requested scope
- greet the author with a wall of context when a short writing cue would do

## Minimal Agent Prompt

Use this when asking an agent to do writing work:

```text
Connect to my repo lewtondoteth/DragonNoir and switch to Writing mode.

Before drafting, follow `notes/writing_workflow.md`.

Identify the scope of the work, load the active canon file, the governing outline, the relevant local notes/scenes/character files, and summarize what already governs this scope. Then continue with the prose work.

Keep the user-facing startup compact: name the active file, give a short cue from the last saved prose, and ask what the author wants to write or change next. Keep the fuller checklist internal unless approval or clarification is needed.

If any relevant scaffold, style, or character-guidance items are not yet approved for drafting use, pause and run the one-by-one approval check before writing.

Before prompting any approval card for a non-canon item, check whether an open issue already tracks it. If the item is approved for this writing pass and no issue exists, preserve it through the correct issue-handoff path after drafting unless I explicitly say not to log it.

If open prose/writing issues contain author-facing draft progress beyond the saved chapter file, build a provisional Forward Draft Context from those issues before asking where to continue. Use it only for drafting continuity; do not treat it as canon or implement it into files unless I explicitly switch to issue implementation or canon update work.

When logging after a writing session that used Forward Draft Context, log only the new delta beyond the saved file and already-open issues. Do not duplicate prose, guidance, or scaffold material that was merely loaded as context.
```
