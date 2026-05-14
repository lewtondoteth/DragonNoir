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

---

# 3. Recommended Issue Shape

An implementation issue should include:

- summary of the desired change
- target file or folder
- canon status: canonical, provisional, experimental, retired, or review-only
- exact material, lines, beats, or discoveries to preserve
- style rules to prioritize
- what not to change
- whether README/path indexes need updating
- acceptance criteria

If the issue comes from exploratory chat, copy in only the chosen material. Do not assume everything discussed in the chat should be implemented.

---

# 4. Agent Rules For Issues

When processing an issue:

1. Read `README.md`.
2. Read `AI_REPO_CONTEXT.md`.
3. Load the story bible, prompt pack, narration rules, and relevant character/profile/outline/note files.
4. Identify the issue type.
5. Stay inside the issue scope.
6. Do not silently promote provisional material to canon.
7. Do not silently clean up unrelated prose or structure.
8. If adding, removing, renaming, or moving files, update the README/file index in the same change.
9. Commit and push only after the acceptance criteria are satisfied.
10. Close the issue only after the completed change is pushed.

If an issue is ambiguous about whether material is canon or provisional, keep it provisional and say so.

---

# 5. Acceptance Criteria Checklist

Use these checks before closing an implementation issue.

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

## Review / Validation

- `git diff --check` passes.
- The final response states what changed, what files were touched, and whether canon was changed or provisional material was promoted.

---

# 6. Review Issues

For review-only issues, acceptance criteria are different:

- no story files edited
- issues are logged with locations or short quoted phrases
- each issue explains the rule, canon point, or style principle involved
- each issue explains the effect on pacing, feel, logic, character, or continuity
- each issue offers suggested resolution directions

Review issues should only be closed after the review report is posted or otherwise captured.
