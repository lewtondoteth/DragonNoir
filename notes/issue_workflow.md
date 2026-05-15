# Issue Workflow

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

This keeps generative conversation, canon decisions, prose integration, and review work separate.

---

# 1. Why Issues Matter

Exploratory work can be messy.

An issue should capture the part that is ready to act on:

- what has been agreed
- what file or section it belongs in
- what material must be preserved
- what should remain undefined
- whether the work is canon, provisional, experimental, or review-only

Implementation agents should treat the issue as scoped instructions, not as permission to broadly rewrite the repo.

If the user asks to "log a ticket", "log an issue", "create an issue", or "make a ticket", create a GitHub issue using the appropriate template in this file. Do not edit repository files as part of issue logging unless the user separately asks for implementation.

---

# 2. Issue Types

## Implementation Issue

Use this when material should be added, revised, moved, or integrated.

The agent may edit files, but only within the issue scope.

## Review Issue

Use this when material should be assessed against the repo rules.

The agent must use the Review Path and stay read-only. It may log detailed issues and suggested fixes, but must not edit prose or resolve the issues itself.

## Planning / Scaffold Issue

Use this when material should be preserved as provisional development material.

The agent may add or update notes, scaffolds, or planning docs, but must not promote the material into canon unless the issue explicitly says to do so.

## Canon Promotion Issue

Use this when provisional material should become active canon.

This must be explicit. Do not infer canon promotion from enthusiasm, repeated discussion, or a polished draft.

## Candidate Rule Issue

Use this when validated rule candidates should be preserved as structured future work without immediately updating canon files.

These issues are for approved candidate guidance that still needs later implementation. They are not proof that the repo has already accepted the rule into canon files.
Do not create a Candidate Rule Issue from an extraction summary alone. Each candidate must first pass the rule-by-rule validation process.

## Candidate Character Guidance Issue

Use this when a validated character-profile item, dynamic note, or bounded character-guidance candidate should be preserved as future work without immediately updating canonical profile files.

These issues are for approved character guidance that still needs later implementation. They are not proof that the repo has already accepted the item into a character profile, story bible, or other canon file.
Do not create a Candidate Character Guidance Issue from exploratory discussion alone. Each candidate must first pass one-by-one approval.

## Candidate Location Guidance Issue

Use this when a validated location-profile item, district note, institution note, or bounded place-guidance candidate should be preserved as future work without immediately updating canonical location files.

These issues are for approved location guidance that still needs later implementation. They are not proof that the repo has already accepted the item into a location profile, story bible, or other canon file.
Do not create a Candidate Location Guidance Issue from exploratory discussion alone. Each candidate must first pass one-by-one approval.

---

# 3. Recommended Issue Shape

An implementation issue should include:

- summary of the desired change
- target file or folder
- target section or insertion point when known
- canon status: canonical, provisional, experimental, retired, or review-only
- exact material, lines, beats, or discoveries to preserve
- style rules to prioritize
- what not to change
- whether README/path indexes need updating
- acceptance criteria

If the issue comes from exploratory chat, copy in only the chosen material. Do not assume everything discussed in the chat should be implemented.

A candidate rule issue should include:

- the validated rule text
- scope: `Global Rule`, `Local Pattern`, or `Scene-Specific Correction`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed rule-by-rule validation before logging
- whether future implementation must re-run manual validation before writing
- what should not yet be treated as canon

A candidate character guidance issue should include:

- the validated character or dynamic guidance text
- scope: `Character Profile Item`, `Dynamic Guidance`, or `Profile Change Candidate`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed one-by-one approval before logging
- whether future implementation must re-run manual validation before writing or profile updates
- what should not yet be treated as canon

A candidate location guidance issue should include:

- the validated location, district, institution, or place-guidance text
- scope: `Location Profile Item`, `District Guidance`, `Institution Guidance`, or `Place Change Candidate`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed one-by-one approval before logging
- whether future implementation must re-run manual validation before writing or profile updates
- what should not yet be treated as canon

If the validated candidate is already adequately represented in the repo, do not create a new issue just to restate it. Prefer:

- no issue
- a refinement note in the extraction or validation report
- a narrowly scoped implementation issue only if there is a genuine gap, ambiguity, missing section, or placement problem to resolve

---

# 4. Drafting-State Protocol

Use explicit drafting states when turning conversation into repo work.

## [EXPLORE]

Free drafting mode.

- Nothing may be treated as canonical.
- No issue creation, file patching, lore promotion, or continuity assumptions should be based on exploratory nouns or plot specifics.
- Newly introduced names, organisations, places, artifacts, lore terms, case terminology, and plot hooks remain volatile.

## [HOLD]

Working material the author currently likes and may continue building around.

- Still non-canonical.
- Stable enough for iterative drafting.
- Not stable enough for continuity anchoring, story-bible updates, or issue implementation unless the user explicitly takes it off hold or asks to implement it.

## [CANON]

Explicitly approved continuity.

- May be committed to files.
- May be referenced by future scenes.
- May be added to story bible, prompt pack, rules, profiles, and issue handoffs as fixed continuity.

## No Accidental Noun Canon

Any newly introduced name, organisation, place, artifact, lore term, case term, or plot mechanism defaults to [EXPLORE] unless explicitly promoted.

When logging drafting discussions, prefer emotional and structural abstractions over implementation-specific nouns if canon status is unclear.

Example:

- Good: "the pink dragon responds with a restrained smile"
- Bad: using an unapproved character name introduced during exploratory drafting

## Pre-Write Verification

Before any repo write action, ask:

> What in this conversation is actually canonical?

Write only what has been approved for the relevant state. If uncertain, generalise and avoid promoting specifics.

---

# 5. Issue Templates

Use these templates when logging GitHub issues.

## Implementation Issue Template

```md
## Type

Implementation

## Target Files

- `path/to/file.md`

## Canon Status

Canonical / Provisional / Experimental / Retired

## Goal

Describe the change to make.

## Material To Preserve

- Specific lines, beats, discoveries, or constraints to keep.

## Style Rules To Prioritize

- Pacing and feel.
- Dragon's first-person noir voice.
- Consequence-first narration.
- Implication-heavy emotional movement.
- Toy-world play-as-reality logic.
- Character/canon constraints relevant to this issue.

## Do Not Change

- Files, sections, canon, plot mechanics, or surrounding prose that should stay untouched.

## Acceptance Criteria

- Scoped requested change is implemented.
- No unrelated prose or structure is rewritten.
- Canon/provisional status is preserved.
- README/file index is updated if paths change.
- `git diff --check` passes.
- Any out-of-scope acceptance gaps are logged as follow-up issues.
```

## Review Issue Template

```md
## Type

Review only

## Target Material

- `path/to/file.md`
- Section, scene, chapter, or quoted passage to review.

## Review Focus

- Pacing and feel.
- Dragon's voice.
- Consequence-first narration.
- Implication-heavy emotional movement.
- Toy-world logic.
- Character consistency.
- Canon/provisional boundary.
- Factual continuity.
- Scene function.

## Relevant References

- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- `rules/noir_narration_rules.md`
- Other relevant character, location, outline, scene, or note files.

## Output Required

Log detailed issues only. Do not edit files.

Each issue should include:

- location or short quoted phrase
- severity or priority
- rule/canon/style conflict
- why it matters
- suggested resolution direction
```

## Planning / Scaffold Issue Template

```md
## Type

Planning / Scaffold

## Target Files

- `notes/name_of_scaffold.md`

## Canon Status

Provisional. Not active canon unless explicitly promoted later.

## Goal

Capture the exploratory structure, beat, idea, object, relationship, or case shape.

## Material To Preserve

- Agreed discoveries or constraints.
- Open possibilities.
- Undefined elements that must remain undefined.

## Do Not Define Yet

- Final plot mechanics.
- Final antagonist.
- Ending.
- Mythology.
- Any canon not explicitly agreed.

## Acceptance Criteria

- Material is captured in notes/scaffolds, not story bible canon.
- Undefined elements remain undefined.
- README/file index is updated if a new file is added.
- `git diff --check` passes.
```

## Canon Promotion Issue Template

```md
## Type

Canon Promotion

## Source Material

- `notes/source_file.md`
- Issue, scene, or discussion source.

## Target Canon Files

- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- Other relevant rules, character, outline, or README files.

## Material To Promote

- Exact facts, rules, beats, or constraints becoming canon.

## Material To Leave Provisional

- Anything not being promoted.

## Reason For Promotion

Why this is now stable enough to become canon.

## Acceptance Criteria

- Promoted material appears in the appropriate canon files.
- Source notes are updated if needed to show what was promoted.
- Prompt pack/rules/character files are updated if they need the new canon.
- README/file index is updated if paths change.
- No unrelated provisional material is promoted.
- `git diff --check` passes.
```

## Candidate Rule Issue Template

```md
## Type

Candidate Rule

## Rule

One validated rule or bounded pattern.

## Scope

Global Rule / Local Pattern / Scene-Specific Correction

## Current State

EXPLORE / HOLD / CANON candidate / unclear

## Source

- Extraction report, chat session, note file, or author review summary

## Evidence Summary

- Short explanation of what author correction, approval, or reasoning supports this candidate.

## Intended Target

- `path/to/file.md`

## Do Not Treat As Final Yet

- Anything that remains unimplemented or unpromoted.

## Acceptance Criteria

- Candidate is preserved accurately.
- Scope is stated clearly.
- Candidate was validated one by one before logging.
- Later implementation repeats the relevant manual validation/checking process before writing.
- No canon files are updated unless separately approved.
```

## Follow-Up Issue Template

```md
## Type

Follow-up

## Origin

- Original issue: #...
- Commit or change that exposed this problem: ...

## What Was Implemented

Briefly describe the completed scoped work.

## Problem Found

Describe the acceptance gap, style issue, canon concern, continuity problem, or review finding.

## Location

- `path/to/file.md`
- Short quoted phrase or section name.

## Why It Matters

Explain how it affects pacing, feel, logic, character, continuity, canon boundaries, or repo maintainability.

## Suggested Resolution Direction

- Possible fix direction.
- Whether this should be review-only or implementation work.

## Acceptance Criteria

- Problem is reviewed or resolved within this issue's scope.
- No unrelated prose or canon is changed.
- `git diff --check` passes if implementation occurs.
```

---

# 5. Agent Rules For Issues

When processing an issue:

1. Read `README.md`.
2. Read `AI_REPO_CONTEXT.md`.
3. Load the story bible, prompt pack, narration rules, and relevant character/location profile, outline, and note files.
4. Identify the issue type.
5. Stay inside the issue scope.
6. Do not silently promote provisional material to canon.
7. Do not silently clean up unrelated prose or structure.
8. If adding, removing, renaming, or moving files, update the README/file index in the same change.
9. Commit and push when the scoped issue work is complete.
10. Run the post-implementation style/flow conflict check.
11. Close the issue only after the completed change is pushed and any acceptance-criteria or style/flow conflicts are either fixed or captured in follow-up issues.

If an issue is ambiguous about whether material is canon or provisional, keep it provisional and say so.

---

# 6. Acceptance Criteria Checklist

Use these checks before closing an implementation issue.

Acceptance criteria are not a reason to silently expand the current issue. If the requested work is implemented but a criterion reveals a remaining problem that cannot be fixed cleanly within the issue scope, allow the work through and log a new follow-up issue.

The original issue may be closed only if:

- the scoped requested work was completed
- any acceptance-criteria failure or style/flow conflict is fixed, or a follow-up issue records it clearly
- the final response names the follow-up issue if one was created

## Scope

- The change is limited to the issue request.
- No unrelated prose has been rewritten.
- No unrelated canon, plot, or structure has been altered.

## Canon / Provisional Boundary

- Canonical material is only changed when the issue explicitly asks for it.
- Provisional material remains in notes/scaffolds unless explicitly promoted.
- Retired material is not revived unless explicitly requested.
- Any canon promotion updates the story bible and prompt pack where needed.

## File Index / Paths

- Any added, removed, renamed, or moved file is reflected in `README.md`.
- Any new workflow or agent rule is reflected in `AI_REPO_CONTEXT.md` and/or `AGENTS.md` if relevant.
- Internal links and relative paths still point to the correct files.

## Prose Style

- The prose matches Dragon's first-person noir voice.
- Pacing and feel remain rain-soaked, patient, implication-heavy, and observational.
- Loaded actions are shown through consequences and object behaviour rather than flat stage directions.
- Emotional movement is implied through behaviour, objects, weather, silence, and practical consequence.
- Humour stays understated and rooted in failed dignity, practical inconvenience, and toy-world logic.

## Character / Continuity

- Dragon remains shabby, vain, treasure-minded, comfort-seeking, water-fearing, dryly funny, and reluctantly brave.
- The pink dragon remains controlled, self-interested, emotionally complicated, and not simply innocent or villainous.
- Toy City play-as-reality logic remains intact.
- Current factual continuity inside active drafts is preserved.

## Post-Implementation Style / Flow Conflict Check

After implementing an issue that changes prose, style rules, narration guidance, character guidance, or scene structure, check whether the change creates a conflict with:

- `rules/noir_narration_rules.md`
- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- relevant character and location profiles
- relevant outlines or active chapter drafts

Look specifically for:

- pacing becoming rushed, over-explained, or mechanically connective
- flat stage directions replacing consequence-first narration in loaded moments
- Dragon's voice becoming too polished, generic, quippy, sentimental, or explanatory
- emotional states being named where implication should carry them
- toy-world play logic being explained, winked at, or made mechanically literal
- character behaviour drifting from established psychology
- provisional material being treated as canon
- new guidance contradicting existing guidance
- active prose now conflicting with newly promoted style rules

If the conflict is small, in-scope, and mechanically fixable, fix it before closing the issue.

If the conflict is real but out of scope, creative, or would require broader revision, create a follow-up issue using the Follow-Up Issue Template.

## Review / Validation

- `git diff --check` passes.
- The final response states what changed, what files were touched, and whether canon was changed or provisional material was promoted.
- The final response states whether a style/flow conflict check was performed and whether follow-up issues were created.

## Follow-Up Issue Rule

Create a follow-up issue instead of broadening the current issue when:

- fixing the problem would require creative judgement beyond the issue scope
- the issue implementation exposed a style, pacing, canon, or continuity problem elsewhere
- the requested change is valid but creates a new concern worth reviewing separately
- acceptance criteria reveal a weakness that is real but not part of the original task
- a post-implementation style/flow conflict check finds a real issue outside the current scope

The follow-up issue should include:

- what was implemented
- what acceptance criterion or repo rule exposed the problem
- where the problem appears
- why it matters
- suggested directions for resolving it
- whether it should be review-only or implementation work

Do not use follow-up issues to avoid fixing simple in-scope problems. Missing README path updates, broken links, failed `git diff --check`, or accidental unrelated edits should usually be fixed before closing the original issue.

---

# 7. Review Issues

For review-only issues, acceptance criteria are different:

- no story files edited
- issues are logged with locations or short quoted phrases
- each issue explains the rule, canon point, or style principle involved
- each issue explains the effect on pacing, feel, logic, character, or continuity
- each issue offers suggested resolution directions

Review issues should only be closed after the review report is posted or otherwise captured.
