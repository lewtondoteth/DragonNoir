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

Weak extraction signals include:

- polished assistant prose without author approval
- speculative assistant summaries
- newly invented names, artifacts, organisations, or plot mechanics without explicit promotion
- broad thematic claims not grounded in a concrete correction or successful passage

## Categories To Extract

### Style Rules

Reusable rules about prose texture, rhythm, narration, humour, pacing, or implication.

Examples:

- case exposition enters sideways
- good scenes trust silence
- Dragon's narration should route emotion through consequence and practical irritation

### Character Behaviour

Reusable rules about how major characters move, think, speak, deflect, manipulate, or reveal themselves.

Examples:

- Dragon physicalises cognition through tail, stuffing, stitching, coffee, and objects
- Odette can take control of a conversation without acknowledging that she has done so

### Scene Patterns

Reusable structures that can guide future drafting.

Example:

1. embodied recognition
2. sensory destabilisation
3. gradual environmental return
4. failed professionalism
5. conversational steering

### Anti-Patterns

Things that made drafts worse or broke the story logic.

Examples:

- direct emotional interpretation before the scene has earned it
- over-explaining why a conversational move is intelligent
- flattening toy-world logic into metaphor
- accidental noun canonisation

### Canon-State Decisions

Classify extracted material as:

- `[EXPLORE]` - volatile, not reusable as continuity
- `[HOLD]` - liked working direction, still not canon
- `[CANON]` - explicitly approved continuity

Do not infer canon promotion from enthusiasm, repeated discussion, or polished wording. Canon promotion must be explicit.

### Exemplars

Short passages or beats that were validated by the author, with a note explaining why they work.

Keep excerpts brief. Prefer small quoted fragments plus commentary over transcript dumping.

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

The report should:

- summarize the source material
- list extracted items by category
- give each item a canon state
- include provenance, such as conversation URL, export filename, date, or author-provided session label
- identify proposed target files
- identify items that require author approval before canon promotion
- recommend follow-up issues when implementation is needed

Do not:

- dump whole transcripts into the repo
- paste long unapproved assistant drafts as exemplars
- promote provisional nouns into canon
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

| Rule | State | Evidence | Suggested Target |
| --- | --- | --- | --- |
|  |  |  |  |

## Character Behaviour

| Rule | Character | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Scene Patterns

| Pattern | State | Evidence | Suggested Target |
| --- | --- | --- | --- |
|  |  |  |  |

## Anti-Patterns

| Anti-pattern | Why It Fails | State | Suggested Target |
| --- | --- | --- | --- |
|  |  |  |  |

## Exemplars

| Fragment | Why It Works | State | Suggested Target |
| --- | --- | --- | --- |
|  |  |  |  |

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

Extract reusable Dragon Noir writing knowledge from author corrections, approvals, rejections, and explanations. Classify every item as [EXPLORE], [HOLD], [CANON], or unclear. Prefer abstraction over transcript dumping. Do not edit canon files or story prose unless I approve the extraction report afterward.
```

For canon promotion after extraction, switch to `notes/rule_validation_workflow.md`.
