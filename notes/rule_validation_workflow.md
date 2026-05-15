# Rule Validation Workflow

Provisional process for turning extracted session knowledge into approved Dragon Noir canon or maintained writing guidance.

This workflow sits after `notes/session_extraction_workflow.md`.

Extraction finds candidate knowledge. Validation asks the author about each candidate rule one at a time. Canon updates happen only after the author has approved, rejected, or corrected the agent's understanding.

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
9. only then update the appropriate repo file

Do not batch-approve rules. One rule means one decision.

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

- `yes` - restate the rule in final form and ask for final approval to update the repo.
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
5. When the author confirms, ask: "Should I add this to `[target file]`?"
6. Write only after explicit approval.
7. After writing, summarize the exact file and section changed.
8. Move to the next candidate.

This is intentionally slower than automated extraction. The slowness protects canon.

## Where Rules Belong

Choose the target file by scope:

- `rules/noir_narration_rules.md` - prose mechanics, voice, pacing, narration, scene handling, recurring drafting anti-patterns
- `characters/pink_dragon_character_profile.md` - Odette-specific psychology, behaviour, manipulation, presentation, relationship dynamics
- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md` - high-level canon, world rules, durable character facts, major project-level constraints
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md` - compact operational guidance agents need during drafting
- `notes/*` - provisional, exploratory, session-specific, or not-yet-canon material

If a rule affects multiple files, validate the rule once, then ask separately about each target update.

## Rule Quality Tests

A validated rule should be:

- reusable across future drafting
- specific enough to guide an agent
- abstract enough not to lock accidental plot details
- supported by author corrections or approved examples
- clear about what not to do
- placed at the right canon level

Reject or hold rules that are:

- just preferences without story impact
- one-off fixes that do not generalize
- assistant inventions without author approval
- provisional nouns disguised as style guidance
- redundant with a clearer existing rule

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

| Rule | Target | Status |
| --- | --- | --- |
|  |  |  |

## Corrected And Pending

| Rule | Correction Needed | Next Question |
| --- | --- | --- |
|  |  |  |

## Rejected

| Rule | Reason |
| --- | --- |
|  |  |

## Hold / Explore

| Rule | State | Where Preserved |
| --- | --- | --- |
|  |  |  |
```

## Minimal Agent Prompt

Use this when asking an agent to validate extracted rules:

```text
Read `README.md`, `AI_REPO_CONTEXT.md`, `notes/issue_workflow.md`, `notes/session_extraction_workflow.md`, and `notes/rule_validation_workflow.md`.

Use the supplied extraction report, notes, or conversation source to identify candidate Dragon Noir rules.

Ask me about one rule at a time using the Candidate Rule Card format:
- rule
- meaning
- works-like examples
- not-like examples
- canon state
- suggested target

Wait for my yes/no/correction. If I correct the explanation, restate it and ask whether you now understand it. Do not add anything to canon files until I explicitly approve that specific rule and target file.
```

Use this when auditing existing rules:

```text
Read `README.md`, `AI_REPO_CONTEXT.md`, `notes/issue_workflow.md`, and `notes/rule_validation_workflow.md`.

Audit `rules/noir_narration_rules.md` one rule at a time. For each rule, explain what you think it means, give a positive example and a negative example, then ask whether to keep, revise, split, merge, move, demote, or remove it. Do not edit the file until I explicitly approve the specific change.
```
