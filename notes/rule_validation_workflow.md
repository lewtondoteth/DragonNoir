# Rule Validation Workflow

Provisional process for turning extracted session knowledge into approved Dragon Noir canon or maintained writing guidance.

This workflow sits after `notes/session_extraction_workflow.md`.

Extraction finds candidate knowledge. Validation asks the author about each candidate rule one at a time. Canon updates happen only after the author has approved, rejected, or corrected the agent's understanding.

This workflow should normally validate `Global Rule` and `Local Pattern` candidates. `Scene-Specific Correction` items usually belong in revision notes, issues, or direct scene work, not canon-rule files.

This workflow may be used in two different ways:

- direct canon update path
- candidate logging path

In the candidate logging path, validation still happens rule by rule, but the approved result is logged into issue-based handoff rather than written into canon files immediately.

## Purpose

Use this workflow when an AI agent has extracted possible rules from notes, session reports, ChatGPT share links, exported logs, or existing repo guidance and the author wants to decide what should become durable guidance.

The agent should act as an interviewer and canon clerk:

1. present one candidate rule
2. explain what it means
3. give positive examples
4. give negative examples
5. ask the author whether the explanation is correct
6. accept correction
7. restate the corrected rule
8. ask for final approval
9. only then update the appropriate repo file or log the approved candidate for later implementation

Do not batch-approve rules. One rule means one decision.

Do not let issue logging replace validation. Logging happens after validation, not instead of it.

## Required References

Before starting, read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/issue_workflow.md`
4. `notes/session_extraction_workflow.md`
5. relevant source notes, extraction reports, story files, rules, profiles, or story-bible sections

Apply the drafting-state protocol throughout.

## Candidate Rule Card

For each candidate, present a compact card in this form:

```md
## Candidate Rule

Rule:
One sentence.

Scope:
`Global Rule (whole story)` / `Local Pattern (current chapter/scene/dynamic)` / `Scene-Specific Correction`

Meaning:
Short explanation in plain language.

Use When:
- Situation where this rule should guide drafting.

Works Like:
- Positive example, beat, or short paraphrased passage.
- Another positive example if useful.

Not Like:
- Negative example or failure mode.
- Another anti-pattern if useful.

Canon State:
[EXPLORE] / [HOLD] / [CANON candidate] / unclear

Suggested Target:
- `rules/noir_narration_rules.md`
- `characters/pink_dragon_character_profile.md`
- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- another specific file

Question:
Is this rule correct as stated?
```

Positive and negative examples may be paraphrased. Use short direct excerpts only when the exact wording matters.

## Author Responses

The agent must handle responses as follows:

- `yes` - restate the rule in final form and ask for final approval to update the repo, if the scope supports canon guidance.
- `yes that's right` in direct canon update path - treat as confirmation of understanding, then ask whether to add it to the target file.
- `yes that's right` in candidate logging path - treat as confirmation of understanding and approval to log it immediately as a candidate issue or preserve it locally, depending on scope.
- `no` - mark the candidate rejected and do not write it into canon.
- correction or clarification - rewrite the rule card using the author's language, then ask again.
- `hold` - record it as `[HOLD]` only if the user wants it preserved; do not add it to canon guidance unless the target file supports provisional material.
- `explore` - keep it out of canon and, if requested, place it in a notes/scaffold file.

The agent must not treat silence, enthusiasm, or discussion as approval.

## Validation Loop

For each candidate rule:

1. Present the candidate rule card.
2. Wait for the author's response.
3. If corrected, restate the revised rule card.
4. Ask: "Do I have that right?"
5. In direct canon update path, when the author confirms, ask: "Should I add this to `[target file]`?"
6. In candidate logging path, `yes that's right` is enough to move straight to logging.
7. After writing or logging, summarize the exact result.
8. Move to the next candidate.

This is intentionally slower than automated extraction. The slowness protects canon.

If the scope is `Scene-Specific Correction`, the default follow-up question should not be about canon files. It should usually be:

> Should I preserve this in a session report, revision note, issue, or chapter note?

## Candidate Logging Path

Use this path when the author says `log that` after an extraction summary or after a validated rule card.

In this mode:

1. validate the candidate rule one by one exactly as usual
2. if the author responds with `yes that's right`, create or update a structured issue rather than immediately editing canon files
3. if the author wants correction first, revise the card and ask again
4. record that later implementation must still repeat the relevant manual checking process before writing

The logging path is for preserving approved candidates and creating a work queue. It is not the same thing as canon promotion.

No issue should be created from an unvalidated candidate. Summary-level extraction output is not enough.

Recommended logging-path confirmation:

> If this is right, say `yes that's right` and I’ll log it.

## Where Rules Belong

Choose the target file by scope:

- `Global Rule`
  `rules/noir_narration_rules.md` - prose mechanics, voice, pacing, narration, scene handling, recurring drafting anti-patterns
  `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md` - high-level canon, world rules, durable character facts, major project-level constraints
  `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md` - compact operational guidance agents need during drafting

- `Local Pattern`
  `characters/pink_dragon_character_profile.md` - Odette-specific psychology, behaviour, manipulation, presentation, relationship dynamics
  chapter outlines, chapter notes, scene-pattern references, or other bounded guidance files
  sometimes `rules/noir_narration_rules.md` if the pattern is clearly reusable across many scenes of the same type

- `Scene-Specific Correction`
  `notes/*`, extraction report, revision note, issue, or direct scene-work context
  not project-wide canon files by default

If a rule affects multiple files, validate the rule once, then ask separately about each target update.

If the user chooses the candidate logging path, the issue should name the intended future target, but the target file should still be treated as pending until implementation is separately approved and checked.

## Rule Quality Tests

A validated rule should be:

- reusable across future drafting
- specific enough to guide an agent
- abstract enough not to lock accidental plot details
- supported by author corrections or approved examples
- clear about what not to do
- placed at the right canon level

A `Local Pattern` should be reusable within a bounded scene family or character dynamic, even if it is not globally portable.

A `Scene-Specific Correction` may be valid and important without qualifying as a durable rule.

Reject or hold rules that are:

- just preferences without story impact
- one-off fixes that do not generalize
- assistant inventions without author approval
- provisional nouns disguised as style guidance
- redundant with a clearer existing rule

Demote candidate rules when:

- they only solve the current paragraph
- they depend too heavily on one object, one beat order, or one exact scene setup
- they would become misleading if applied elsewhere

## Existing Rule Audit

Use this path when the author wants to review the current rule system.

The agent should:

1. Read the current target file, such as `rules/noir_narration_rules.md`.
2. Split it into individual auditable rules.
3. Convert each rule into the candidate card format.
4. Ask the author about one rule at a time.
5. Track each rule as:
   - keep
   - revise
   - split
   - merge
   - move
   - demote to notes
   - remove
6. Apply edits only after explicit approval for the specific rule or section.

Audit questions should focus on whether the rule is still true, clear, useful, and placed in the correct file.

## Audit Card

```md
## Existing Rule Audit

Current Rule:
Quoted or paraphrased rule.

Current Location:
`path/to/file.md`

My Understanding:
What I think this rule means.

Works Like:
- Positive example.

Not Like:
- Negative example.

Recommendation:
Keep / revise / split / merge / move / demote / remove.

Question:
Is my understanding right, and what should happen to this rule?
```

## Output Log

For long validation sessions, maintain a temporary report before editing canon files:

```md
# Rule Validation Report

## Source

- Extraction report, chat link, notes file, or target audit file:

## Approved For Canon

| Rule | Scope | Target | Status |
| --- | --- | --- | --- |
|  |  |  |  |

## Corrected And Pending

| Rule | Scope | Correction Needed | Next Question |
| --- | --- | --- | --- |
|  |  |  |  |

## Rejected

| Rule | Scope | Reason |
| --- | --- | --- |
|  |  |  |

## Hold / Explore

| Rule | Scope | State | Where Preserved |
| --- | --- | --- | --- |
|  |  |  |  |

## Scene-Specific Corrections

| Correction | Preserve Where | Status |
| --- | --- | --- |
|  |  |  |

## Logged For Later

| Rule | Scope | Intended Target | Issue |
| --- | --- | --- | --- |
|  |  |  |  |
```

## Minimal Agent Prompt

Use this when asking an agent to validate extracted rules:

```text
Read `README.md`, `AI_REPO_CONTEXT.md`, `notes/issue_workflow.md`, `notes/session_extraction_workflow.md`, and `notes/rule_validation_workflow.md`.

Use the supplied extraction report, notes, or conversation source to identify candidate Dragon Noir rules.

Ask me about one rule at a time using the Candidate Rule Card format:
- rule
- scope
- meaning
- works-like examples
- not-like examples
- canon state
- suggested target

Wait for my yes/no/correction. If I correct the explanation, restate it and ask whether you now understand it. Do not add anything to canon files until I explicitly approve that specific rule and target file. If the candidate is really only a Scene-Specific Correction, preserve it locally instead of treating it as canon guidance. If I say `log that`, use the candidate logging path rather than assuming direct canon edits.
```

Use this when auditing existing rules:

```text
Read `README.md`, `AI_REPO_CONTEXT.md`, `notes/issue_workflow.md`, and `notes/rule_validation_workflow.md`.

Audit `rules/noir_narration_rules.md` one rule at a time. For each rule, explain what you think it means, give a positive example and a negative example, then ask whether to keep, revise, split, merge, move, demote, or remove it. Do not edit the file until I explicitly approve the specific change.
```
