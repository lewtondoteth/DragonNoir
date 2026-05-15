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

When implementing this issue type, the agent must use the `Implementation Wizard` before making changes.

## Review Issue

Use this when material should be assessed against the repo rules.

The agent must use the Review Path and stay read-only. It may log detailed issues and suggested fixes, but must not edit prose or resolve the issues itself.

## Consistency Fix Issue

Use this when review, profile scan, character scan, consistency scan, or writing follow-up work identifies a real clash, contradiction, profile gap, or location-logic mismatch that should be repaired later.

These issues are for fixable inconsistencies or missing bounded guidance. They are not permission to rewrite the repo immediately.

When implementing this issue type, the agent must use the `Implementation Wizard` before making changes.

## Planning / Scaffold Issue

Use this when material should be preserved as provisional development material.

The agent may add or update notes, scaffolds, or planning docs, but must not promote the material into canon unless the issue explicitly says to do so.

If this issue will change repo files rather than only log planning material, the agent must use the `Implementation Wizard` before making changes.

## Canon Promotion Issue

Use this when provisional material should become active canon.

This must be explicit. Do not infer canon promotion from enthusiasm, repeated discussion, or a polished draft.

When implementing this issue type, the agent must use the `Implementation Wizard` before making changes.

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

## Candidate Case Guidance Issue

Use this when a validated case-profile item or bounded case-guidance candidate should be preserved as future work without immediately updating canonical case files.

These issues are for approved case guidance that still needs later implementation. They are not proof that the repo has already accepted the item into a case profile, story bible, or other canon file.
Do not create a Candidate Case Guidance Issue from exploratory discussion alone. Each candidate must first pass one-by-one approval.

## Candidate Object Guidance Issue

Use this when a validated object-profile item or bounded object-guidance candidate should be preserved as future work without immediately updating canonical object files.

These issues are for approved object guidance that still needs later implementation. They are not proof that the repo has already accepted the item into an object profile, story bible, or other canon file.
Do not create a Candidate Object Guidance Issue from exploratory discussion alone. Each candidate must first pass one-by-one approval.

## Candidate Organisation Guidance Issue

Use this when a validated organisation-profile item or bounded organisation-guidance candidate should be preserved as future work without immediately updating canonical organisation files.

These issues are for approved organisation guidance that still needs later implementation. They are not proof that the repo has already accepted the item into an organisation profile, story bible, or other canon file.
Do not create a Candidate Organisation Guidance Issue from exploratory discussion alone. Each candidate must first pass one-by-one approval.

## Shared Dedupe Rule

Before logging any new issue from Review, Session Extraction, Profile Pull, Character Scan, Consistency Scan, Scaffold Capture, or Writing follow-up preservation:

1. check whether an open issue already tracks the same scope
2. if yes, reference the existing issue instead of creating a duplicate
3. only create a new issue when there is a genuinely new unresolved repo task

---

# 3. Recommended Issue Shape

## Implementation Wizard

When the user asks an agent to process, resolve, implement, or close an issue, the agent must not jump straight into editing.

It must enter an explicit `Implementation Wizard`.

The purpose of the wizard is:

1. break the issue into concrete proposed changes
2. show those changes to the user one by one
3. get approval before each change is made
4. keep the implementation from silently broadening

### Wizard Steps

For issue implementation work:

1. read the issue carefully
2. inspect the relevant repo files
3. produce a short `Planned Changes` list
4. convert that list into one or more `Change Cards`
5. present the cards one at a time
6. wait for the user's response before editing
7. only make the approved change
8. then move to the next card

Do not batch unrelated edits into one approval.

### Change Card

Each proposed change should be presented in a compact card:

```md
## Proposed Change

Issue:
#123

Target:
`path/to/file.md`

Change:
One concrete thing to add, revise, move, or remove.

Why:
Why this change is needed to satisfy the issue.

Scope Check:
What this change will not touch.

Question:
Approve this change?
```

### Allowed User Responses

The user should be able to answer in plain language, for example:

- `yes`
- `yes that's right`
- `no`
- `skip that`
- `correct: ...`

If the user corrects the description, the agent must restate the corrected change before editing.

### Default Rule

Approval of the issue as a whole is not approval of each concrete file change.

The agent must obtain approval for each concrete change before making it.

### After Each Approved Change

After making an approved change, the agent should:

1. summarize what changed
2. say which issue card it satisfied
3. present the next proposed change card, if any

### Closing Rule

An implementation issue should only be closed after:

- every approved change card has been applied
- skipped or rejected cards are clearly noted
- acceptance criteria are checked
- any out-of-scope findings are logged as follow-up issues

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

A candidate case guidance issue should include:

- the validated case guidance text
- scope: `Case Profile Item`, `Case Logic`, or `Case Change Candidate`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed one-by-one approval before logging
- whether future implementation must re-run manual validation before writing or case-profile updates
- what should not yet be treated as canon

A candidate object guidance issue should include:

- the validated object guidance text
- scope: `Object Profile Item`, `Object Logic`, or `Object Change Candidate`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed one-by-one approval before logging
- whether future implementation must re-run manual validation before writing or object-profile updates
- what should not yet be treated as canon

A candidate organisation guidance issue should include:

- the validated organisation guidance text
- scope: `Organisation Profile Item`, `Organisation Logic`, or `Organisation Change Candidate`
- current canon state
- source or evidence summary
- intended future target file
- intended future target section or placement when known
- confirmation that the candidate passed one-by-one approval before logging
- whether future implementation must re-run manual validation before writing or organisation-profile updates
- what should not yet be treated as canon

If the validated candidate is already adequately represented in the repo, do not create a new issue just to restate it. Prefer:

- no issue
- a refinement note in the extraction or validation report
- a narrowly scoped implementation issue only if there is a genuine gap, ambiguity, missing section, or placement problem to resolve

All issue types should also include, when known:

- existing matching issue check result
- recommended labels

## Recommended Labels

Use labels consistently when the repository or GitHub setup supports them.

### Mode Labels

- `mode:writing`
- `mode:review`
- `mode:session-extraction`
- `mode:profile-scan`
- `mode:scaffold-capture`
- `mode:issue-work`

### Type Labels

- `type:implementation`
- `type:review`
- `type:scaffold`
- `type:canon-promotion`
- `type:candidate-rule`
- `type:candidate-character`
- `type:candidate-location`
- `type:candidate-case`
- `type:candidate-object`
- `type:candidate-organisation`
- `type:consistency-fix`

### Scope Labels

Use narrow scope labels when they help prevent duplication, for example:

- `scope:chapter-1`
- `scope:dragon-office`
- `scope:toy-city`
- `scope:odette`

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

## Recommended Labels

- `type:implementation`
- `scope:...`

## Target Files

- `path/to/file.md`

## Canon Status

Canonical / Provisional / Experimental / Retired

## Goal

Describe the change to make.

## Implementation Wizard

- Break the issue into concrete change cards before editing.
- Present each proposed change one by one.
- Get explicit approval before each change is made.
- Restate corrections before editing if the user adjusts the card.

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
- Each concrete change was approved through the Implementation Wizard before being made.
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

## Recommended Labels

- `mode:review`
- `type:review`
- `scope:...`

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
- Tone consistency.
- Location consistency.

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

## Consistency Fix Issue Template

```md
## Type

Consistency Fix

## Recommended Labels

- `mode:review` or `mode:profile-scan`
- `type:consistency-fix`
- `scope:...`

## Target Material

- `path/to/file.md`
- profile, location, outline, or draft area where the clash appears

## Conflict Summary

Describe the contradiction, mismatch, or missing bounded guidance.

## Conflicts With

- `path/to/reference.md`
- specific profile, rule, location, or canon point

## Why It Matters

- tone / continuity / motive / action / spatial logic / canon integrity

## Clarification Status

- confirmed by author
- still needs one clarification
- inferred from repo comparison only

## Suggested Repair Direction

- update the draft
- update the profile
- add bounded guidance
- revise the outline

## Acceptance Criteria

- issue states the clash clearly
- conflicting references are named
- duplicate check was performed
- no repo files are edited during issue logging
```

## Planning / Scaffold Issue Template

```md
## Type

Planning / Scaffold

## Recommended Labels

- `mode:scaffold-capture`
- `type:scaffold`
- `scope:...`

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

## Recommended Labels

- `type:canon-promotion`
- `scope:...`

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

## Recommended Labels

- `mode:session-extraction`
- `type:candidate-rule`
- `scope:...`

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

## Candidate Character Guidance Issue Template

```md
## Type

Candidate Character Guidance

## Recommended Labels

- `mode:session-extraction` or `mode:profile-scan`
- `type:candidate-character`
- `scope:...`

## Guidance

One validated character-profile, dynamic, or behavior-guidance item.

## Scope

`Character Profile Item` / `Dynamic Guidance` / `Profile Change Candidate`

## Current State

`[EXPLORE]` / `[HOLD]` / `CANON candidate`

## Source

- Session extraction, validation session, or other approved source.

## Evidence Summary

- Short explanation of what the author approved and why it matters.

## Intended Target

- `characters/path_to_profile.md`
- Suggested placement or section when known

## Do Not Treat As Final Yet

- No profile or canon files are updated during issue logging.
- Later implementation must repeat the relevant manual validation/checking process before writing or profile updates.

## Acceptance Criteria

- Candidate guidance is preserved accurately.
- Scope is stated clearly.
- Candidate passed one-by-one approval before logging.
- No canon files are updated unless separately approved.
```

## Candidate Location Guidance Issue Template

```md
## Type

Candidate Location Guidance

## Recommended Labels

- `mode:session-extraction` or `mode:profile-scan`
- `type:candidate-location`
- `scope:...`

## Guidance

One validated location-profile, district, institution, or place-guidance item.

## Scope

`Location Profile Item` / `District Guidance` / `Institution Guidance` / `Place Change Candidate`

## Current State

`[EXPLORE]` / `[HOLD]` / `CANON candidate`

## Source

- Session extraction, validation session, or other approved source.

## Evidence Summary

- Short explanation of what the author approved and why it matters.

## Intended Target

- `locations/path_to_location_profile.md`
- Suggested placement or section when known

## Do Not Treat As Final Yet

- No location profile or canon files are updated during issue logging.
- Later implementation must repeat the relevant manual validation/checking process before writing or profile updates.

## Acceptance Criteria

- Candidate guidance is preserved accurately.
- Scope is stated clearly.
- Candidate passed one-by-one approval before logging.
- No canon files are updated unless separately approved.
```

## Candidate Case Guidance Issue Template

```md
## Type

Candidate Case Guidance

## Recommended Labels

- `mode:session-extraction`, `mode:profile-scan`, or `mode:scaffold-capture`
- `type:candidate-case`
- `scope:...`

## Guidance

One validated case-profile, case-logic, or case-guidance item.

## Scope

`Case Profile Item` / `Case Logic` / `Case Change Candidate`

## Current State

`[EXPLORE]` / `[HOLD]` / `CANON candidate`

## Source

- Session extraction, scaffold capture, validation session, or other approved source.

## Evidence Summary

- Short explanation of what the author approved and why it matters.

## Intended Target

- `cases/path_to_case_profile.md`
- Suggested placement or section when known

## Do Not Treat As Final Yet

- No case profile or canon files are updated during issue logging.
- Later implementation must repeat the relevant manual validation/checking process before writing or case-profile updates.

## Acceptance Criteria

- Candidate guidance is preserved accurately.
- Scope is stated clearly.
- Candidate passed one-by-one approval before logging.
- No canon files are updated unless separately approved.
```

## Candidate Object Guidance Issue Template

```md
## Type

Candidate Object Guidance

## Recommended Labels

- `mode:session-extraction`, `mode:profile-scan`, or `mode:scaffold-capture`
- `type:candidate-object`
- `scope:...`

## Guidance

One validated object-profile or object-guidance item.

## Scope

`Object Profile Item` / `Object Logic` / `Object Change Candidate`

## Current State

`[EXPLORE]` / `[HOLD]` / `CANON candidate`

## Source

- Session extraction, scaffold capture, validation session, or other approved source.

## Evidence Summary

- Short explanation of what the author approved and why it matters.

## Intended Target

- `objects/path_to_object_profile.md`
- Suggested placement or section when known

## Do Not Treat As Final Yet

- No object profile or canon files are updated during issue logging.
- Later implementation must repeat the relevant manual validation/checking process before writing or object-profile updates.

## Acceptance Criteria

- Candidate guidance is preserved accurately.
- Scope is stated clearly.
- Candidate passed one-by-one approval before logging.
- No canon files are updated unless separately approved.
```

## Candidate Organisation Guidance Issue Template

```md
## Type

Candidate Organisation Guidance

## Recommended Labels

- `mode:session-extraction`, `mode:profile-scan`, or `mode:scaffold-capture`
- `type:candidate-organisation`
- `scope:...`

## Guidance

One validated organisation-profile or organisation-guidance item.

## Scope

`Organisation Profile Item` / `Organisation Logic` / `Organisation Change Candidate`

## Current State

`[EXPLORE]` / `[HOLD]` / `CANON candidate`

## Source

- Session extraction, scaffold capture, validation session, or other approved source.

## Evidence Summary

- Short explanation of what the author approved and why it matters.

## Intended Target

- `organisations/path_to_organisation_profile.md`
- Suggested placement or section when known

## Do Not Treat As Final Yet

- No organisation profile or canon files are updated during issue logging.
- Later implementation must repeat the relevant manual validation/checking process before writing or organisation-profile updates.

## Acceptance Criteria

- Candidate guidance is preserved accurately.
- Scope is stated clearly.
- Candidate passed one-by-one approval before logging.
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
