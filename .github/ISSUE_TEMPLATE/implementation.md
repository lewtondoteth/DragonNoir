---
name: Implementation
about: Add, revise, move, or integrate scoped repo material
title: "Implement: "
labels: "type:implementation"
---

## Type

Implementation

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

## Source Prose

- Exact wording to integrate, if prose exists.
- Include only prose the author has explicitly approved for integration.
- If this section is empty, the issue contains beats only and does not authorize reconstructed prose unless explicitly stated in the Goal.

## Diagnostic Excerpts / Rejected Drafts

- Pasted prose used as evidence, comparison, review material, complaint context, or rejected wording.
- Do not integrate this material unless it is separately promoted into Source Prose by explicit author instruction.

## Beats / Intent

- Summary beats, scene intent, or functional requirements.
- Keep these separate from exact wording.

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
- Exact prose and beat summaries are kept distinct; reconstructed prose is used only with explicit approval.
- Diagnostic excerpts, rejected drafts, and disputed pasted material are not integrated as source prose.
- If prose is added or revised, loaded beats are checked against maintained narration rules, especially implication-heavy/consequence-first narration.
- If prose contains direct emotional or social labels in loaded moments, either revise them into observable behaviour/object consequence/Dragon-filtered image or log a follow-up if the defect is out of scope.
- README/file index is updated if paths change.
- `git diff --check` passes.
- Any out-of-scope acceptance gaps are logged as follow-up issues.
