# Session Extraction Workflow

Provisional process design for extracting reusable Dragon Noir writing knowledge from shared ChatGPT conversations or exported conversation logs.

This workflow is deliberately lightweight. It is an AI-assisted reading protocol, not an automated ingestion system. The goal is to preserve durable narrative intelligence without dumping transcripts into the repository or accidentally promoting exploratory material into canon.

## Purpose

Use this workflow when the author provides a ChatGPT share URL, exported conversation log, pasted transcript, or similar writing-session record and asks an agent to extract reusable project knowledge.

The agent should look for:

- corrections from the author
- rejected drafts and the reasons they failed
- approved phrasings, beats, or structural moves
- explanations of why a version worked
- emergent style rules
- character behaviour discoveries
- scene mechanics
- anti-patterns
- canon, hold, or explore-state decisions
- continuity risks
- process improvements for future sessions

The valuable material is usually the reasoning around a draft, not the transcript itself.

## Scope Classification

Before treating any extracted item as guidance, classify its scope.

Every extracted item should be tagged as one of:

- `Global Rule`
- `Local Pattern`
- `Scene-Specific Correction`

This classification happens before canon-state handling.

### Global Rule

Use this for guidance that should travel well across the project.

A Global Rule should still help in a different chapter with different objects, scene furniture, and stakes.

Examples:

- consequence-first narration
- case exposition enters sideways
- good scenes trust silence

### Local Pattern

Use this for guidance that is reusable, but only inside a certain scene type, character dynamic, chapter function, or structural position.

A Local Pattern may be valuable without being universal.

Examples:

- in Dragon/Odette recognition scenes, similarity should emerge through observed effects before explicit comparison
- after an uncanny reveal, Dragon may re-enter cognition through physical consequence and environmental return

### Scene-Specific Correction

Use this for guidance that fixes the current passage but should not be generalized automatically.

Scene-Specific Corrections are often highly valuable for revision, but destructive if promoted too early into rule files.

Examples:

- this coffee sequence is overstaying its welcome
- this paragraph names the intelligence of the moment too directly
- this beat should stay in Chapter 1 notes rather than become a project rule

### Scope Test

Ask:

> Would this still help in a different chapter with different objects and stakes?

If yes, it may be a `Global Rule`.

If sometimes, it is probably a `Local Pattern`.

If no, it is probably a `Scene-Specific Correction`.

## Inputs

Acceptable inputs:

- ChatGPT shared conversation URL
- exported ChatGPT conversation log
- pasted transcript
- selected excerpts from a conversation
- author summary of a session

If the agent cannot access a shared URL, it should ask the author for an export, paste, or selected excerpts rather than guessing.

## Required References

Before extraction, read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/issue_workflow.md`
4. Relevant canon or style files if the session touches them:
   - `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
   - `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
   - `rules/noir_narration_rules.md`
   - relevant character profiles, chapter drafts, scene drafts, outlines, or notes

Apply the drafting-state protocol from `AI_REPO_CONTEXT.md` and `notes/issue_workflow.md` throughout.

## Extraction Priorities

Prioritize author judgement over assistant output.

Strong extraction signals include:

- the author says a beat works
- the author explains why a beat works
- the author rejects a draft and names the failure mode
- the author corrects tone, character logic, pacing, or canon
- the session discovers a repeatable scene pattern
- the session identifies a failure that should be avoided later
- the author explicitly marks material as `[EXPLORE]`, `[HOLD]`, or `[CANON]`

Even strong signals still require scope classification. A strong correction may still be only a Scene-Specific Correction.

Weak extraction signals include:

- polished assistant prose without author approval
- speculative assistant summaries
- newly invented names, artifacts, organisations, or plot mechanics without explicit promotion
- broad thematic claims not grounded in a concrete correction or successful passage
- highly local revision fixes being overstated as project-wide rules

## Categories To Extract

### Style Rules

Reusable rules about prose texture, rhythm, narration, humour, pacing, or implication.

Examples:

- case exposition enters sideways
- good scenes trust silence
- Dragon's narration should route emotion through consequence and practical irritation

These should normally classify as `Global Rule` or `Local Pattern`, not `Scene-Specific Correction`.

### Character Behaviour

Reusable rules about how major characters move, think, speak, deflect, manipulate, or reveal themselves.

Examples:

- Dragon physicalises cognition through tail, stuffing, stitching, coffee, and objects
- Odette can take control of a conversation without acknowledging that she has done so

These often classify as `Global Rule` or `Local Pattern`.

### Scene Patterns

Reusable structures that can guide future drafting.

Example:

1. embodied recognition
2. sensory destabilisation
3. gradual environmental return
4. failed professionalism
5. conversational steering

These often classify as `Local Pattern`.

### Anti-Patterns

Things that made drafts worse or broke the story logic.

Examples:

- direct emotional interpretation before the scene has earned it
- over-explaining why a conversational move is intelligent
- flattening toy-world logic into metaphor
- accidental noun canonisation

These may classify at any scope level.

### Canon-State Decisions

Classify extracted material as:

- `[EXPLORE]` - volatile, not reusable as continuity
- `[HOLD]` - liked working direction, still not canon
- `[CANON]` - explicitly approved continuity

Do not infer canon promotion from enthusiasm, repeated discussion, or polished wording. Canon promotion must be explicit.

Do not infer that a `Scene-Specific Correction` belongs in canon guidance merely because its correction was strongly argued.

### Exemplars

Short passages or beats that were validated by the author, with a note explaining why they work.

Keep excerpts brief. Prefer small quoted fragments plus commentary over transcript dumping.

Exemplars may support a `Global Rule` or `Local Pattern`, or remain attached to a `Scene-Specific Correction`.

### Continuity Risks

Risks discovered during the session.

Examples:

- a provisional name may be mistaken for canon
- a case object may accidentally lock the whole plot too early
- a scene may drift from Toy Noir into adult noir parody
- Dragon may become too articulate about his own emotions

### Process Improvements

Workflow lessons that should improve future AI-assisted sessions.

Examples:

- ask for canon state before logging issues from exploratory drafting
- preserve review-only findings as issues, not silent rewrites
- separate accepted prose from accepted reasoning

## Output Rules

The first output should usually be an extraction report, not direct edits to canon files.

After extraction, use `notes/rule_validation_workflow.md` before promoting candidate rules into canon or maintained guidance.

If the author says `log that` after reviewing the extraction summary, the agent should not jump straight into canon edits. It should treat that as permission to begin a rule-by-rule validation and logging pass.

The report should:

- summarize the source material
- list extracted items by category
- classify the scope of each item before treating it as guidance
- give each item a canon state
- include provenance, such as conversation URL, export filename, date, or author-provided session label
- identify proposed target files
- identify items that require author approval before canon promotion
- recommend follow-up issues when implementation is needed

## `Log That` Handoff

If the author responds to an extraction summary with something like:

- `log that`
- `ok log that`
- `turn that into issues`
- `capture those`

the agent should interpret it as:

1. preserve the extracted candidates
2. begin rule-by-rule validation
3. only after each individual rule passes validation, log that approved item in a structured issue or issues
4. avoid direct canon edits unless separately approved

The agent should not treat `log that` as permission to silently write the extracted rules into canon files.
The agent should also not create candidate-rule issues from the summary alone. Each issue-worthy item must first survive the one-by-one check.

Recommended behavior:

- `Global Rule` and `Local Pattern`
  Present them one by one through `notes/rule_validation_workflow.md`

- `Scene-Specific Correction`
  Preserve them in extraction notes, revision notes, or issue context rather than forcing them through canon validation

After validation, the agent may log the approved candidates as issue-based implementation work, but the later implementation step must still repeat the relevant manual checks before any canon file is changed.

Do not:

- dump whole transcripts into the repo
- paste long unapproved assistant drafts as exemplars
- promote provisional nouns into canon
- turn local revision advice into project-wide rules without a scope test
- rewrite story files during extraction unless the user separately asks for implementation
- overwrite existing rules without explaining what changed
- skip rule-by-rule author validation when turning extracted knowledge into canon guidance

## Extraction Report Template

```md
# Session Extraction Report

## Source

- Link or file:
- Session date:
- Extracted by:
- Scope requested:

## Summary

Briefly describe what the conversation was about and what kind of reusable knowledge it produced.

## Canon-State Overview

- [CANON]:
- [HOLD]:
- [EXPLORE]:
- Unclear / needs author decision:

## Style Rules

| Rule | Scope | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Character Behaviour

| Rule | Character | Scope | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Scene Patterns

| Pattern | Scope | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Anti-Patterns

| Anti-pattern | Scope | Why It Fails | State | Suggested Target |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Scene-Specific Corrections

| Correction | Why It Matters Here | State | Suggested Target |
| --- | --- | --- | --- |
|  |  |  |  |

## Exemplars

| Fragment | Supports | Scope | Why It Works | State | Suggested Target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Continuity Risks

| Risk | Location / Evidence | Suggested Handling |
| --- | --- | --- |
|  |  |  |

## Recommended Repo Updates

- 

## Follow-Up Issues To Log

- 

## Do Not Promote Yet

- 
```

## Candidate Logging Output

When the author wants the extracted material logged rather than immediately implemented, prefer creating one or more issues that preserve:

- the approved rule text
- scope
- canon state
- evidence summary
- suggested target file
- whether the future implementation must re-run validation before writing

Logged candidate issues are handoff containers, not proof that the rule is already canon.

## Target Guidance By Scope

Use scope to constrain where extracted items should go.

- `Global Rule`
  Usual targets: `rules/noir_narration_rules.md`, story bible, prompt pack, durable character profiles

- `Local Pattern`
  Usual targets: chapter outlines, character profiles, chapter-specific notes, scene-pattern references

- `Scene-Specific Correction`
  Usual targets: extraction report, issue, chapter note, revision note, or direct scene work

Scene-Specific Corrections should not go into project-wide canon-rule files by default.

## Suggested Knowledge Targets

If extraction becomes frequent, create a dedicated knowledge area such as:

```text
docs/
├── STYLE_RULES.md
├── CHARACTER_BEHAVIOUR.md
├── SCENE_PATTERNS.md
├── ANTI_PATTERNS.md
├── HOLD_CONCEPTS.md
├── EXEMPLARS.md
└── CONTINUITY_RULES.md
```

Do not create these files merely because a session exists. Add them when repeated extraction produces enough durable material to justify separate maintained references.

## Minimal Agent Prompt

Use this when asking an AI agent to extract a session:

```text
Read `README.md`, `AI_REPO_CONTEXT.md`, `notes/issue_workflow.md`, and `notes/session_extraction_workflow.md`.

Then review this ChatGPT conversation link or exported transcript:

[source here]

Extract reusable Dragon Noir writing knowledge from author corrections, approvals, rejections, and explanations. For every item, first classify scope as `Global Rule`, `Local Pattern`, or `Scene-Specific Correction`, then classify canon state as [EXPLORE], [HOLD], [CANON], or unclear. Prefer abstraction over transcript dumping. Do not edit canon files or story prose unless I approve the extraction report afterward. If I say `log that`, move into rule-by-rule validation and structured candidate logging rather than direct canon edits.
```

For canon promotion after extraction, switch to `notes/rule_validation_workflow.md`.
