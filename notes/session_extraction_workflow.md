# Session Extraction Workflow

Provisional process design for extracting reusable Dragon Noir knowledge from shared ChatGPT conversations or exported conversation logs.

This workflow is deliberately lightweight. It is an AI-assisted reading protocol, not an automated ingestion system. The goal is to preserve durable narrative intelligence without dumping transcripts into the repository or accidentally promoting exploratory material into canon.

Extraction should happen in one pass.

The agent should not require separate passes for rules, scaffolds, and character guidance if the same session contains all three. Instead, it should do one classification pass, identify all capture-worthy items, and sort them into the correct lanes for validation, logging, or later writing use.

## Purpose

Use this workflow when the author provides a ChatGPT share URL, exported conversation log, pasted transcript, or similar writing-session record and asks an agent to extract reusable Dragon Noir knowledge.

The intended flow is:

1. write or brainstorm in a separate chat
2. export or attach that chat log
3. connect to the repo
4. switch into `Session Extraction`
5. let the extraction agent read the finished session as source material

This keeps drafting and extraction as separate roles with different goals.

The agent should look for:

- corrections from the author
- rejected drafts and the reasons they failed
- approved phrasings, beats, or structural moves
- explanations of why a version worked
- emergent style rules
- character behaviour discoveries
- scene mechanics
- plot directions and scaffolds
- candidate profile changes or dynamic guidance
- candidate location-profile changes or place guidance
- candidate case-profile changes or case guidance
- candidate object-profile changes or object guidance
- candidate organisation-profile changes or organisation guidance
- spatial characteristics that may belong in location profiles
- anti-patterns
- canon, hold, or explore-state decisions
- continuity risks
- process improvements for future sessions

The valuable material is usually the reasoning around a draft, not the transcript itself.

This mode is for knowledge extraction, not prose extraction. It may identify rule candidates, local patterns, character guidance, location guidance, case guidance, object guidance, organisation guidance, and scaffold material in the same pass, but it should not jump straight into prose generation or canon edits unless the author explicitly switches modes.

The extraction agent should behave like a post-writing analyst, not like the original drafting partner.

The default preservation path is issue-first:

1. extract and classify
2. validate worthwhile items one by one
3. log the approved result using the appropriate issue type
4. implement later only if the author explicitly asks

## One-Pass Multi-Track Extraction

Run one extraction pass and classify each worthwhile item by both `Type` and `Scope`.

### Type Classification

Every extracted item should first be tagged as one of:

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

### Route By Type

After classification:

- `Global Rule` -> rule validation path
- `Local Pattern` -> rule validation path or bounded local guidance path
- `Character Guidance` -> one-by-one approval, then profile/dynamic guidance logging or update path
- `Location Guidance` -> one-by-one approval, then location-guidance logging or profile update path
- `Case Guidance` -> one-by-one approval, then case-guidance logging or case-profile update path
- `Object Guidance` -> one-by-one approval, then object-guidance logging or object-profile update path
- `Organisation Guidance` -> one-by-one approval, then organisation-guidance logging or organisation-profile update path
- `Scaffold Material` -> scaffold capture or planning/scaffold issue path
- `Scene-Specific Correction` -> exclude from default triage unless explicitly requested
- `Process Improvement` -> preserve in workflow/notes only if the author wants it kept

The agent should not make the author run the same source material through three separate extraction requests just because the session produced more than one kind of useful knowledge.

## Scope Classification

Before treating any extracted item as guidance, classify its scope.

Every extracted item should also be tagged by scope as one of:

- `Global Rule`
- `Local Pattern`
- `Scene-Specific Correction`

This classification happens before canon-state handling.

The `Type` and `Scope` are related, but not identical.

Examples:

- a `Character Guidance` item may have `Local Pattern` scope
- a `Location Guidance` item may have `Local Pattern` scope
- a `Case Guidance`, `Object Guidance`, or `Organisation Guidance` item may have `Local Pattern` scope
- a `Scaffold Material` item may be chapter-scoped rather than project-wide
- a `Global Rule` item is usually also global in scope

## Entity Growth Check

When a session produces durable information about a named or strongly implied entity, the extraction pass should ask:

1. what kind of entity is this?
   - character
   - location
   - case
   - object
   - organisation
2. does a canon surface for it already exist in the repo?
3. if yes, is this:
   - already represented
   - a refinement
   - a real new addition
4. if no, is there enough durable information to justify establishing a new canon surface later?

If an entity surface already exists, the default is:

- enrich that existing surface through validated issue logging or direct implementation when requested

If an entity surface does not exist yet, the default is:

- log the correct candidate issue so the entity can be established cleanly later

Do not silently promote a newly mentioned thief, organisation, object, or case noun into canon just because the chat made it vivid.

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

Use this only as a rejection bucket during extraction triage.

Scene-Specific Corrections may be recognized so they can be excluded from rule extraction. They should not be expanded in this mode unless the author explicitly asks to see local corrections.

### Scope Test

Ask:

> Would this still help in a different chapter with different objects and stakes?

If yes, it may be a `Global Rule`.

If sometimes, it is probably a `Local Pattern`.

If no, it is probably a `Scene-Specific Correction`, which means it is usually out of scope for default rule extraction output.

## Accepted Prose Beat vs Reusable Guidance

When extracting from a drafting session, do not assume that an accepted line, beat, or correction is reusable guidance.

First ask what the author's approval actually means:

1. this exact prose or beat should be used in the current draft
2. this is a scene-specific correction or implementation texture
3. this is a local pattern that may help future similar scenes
4. this is a global rule or character-guidance candidate

Accepted prose belongs in the relevant implementation issue or current draft, not in rule guidance, unless it survives the scope test.

Scene-specific corrections should usually stay attached to the implementation issue or draft they belong to.

Examples of things that are often accepted prose beats rather than reusable guidance:

- a redirected question in one specific exchange
- a silence, cup turn, pause, or stillness beat that only solves the current scene
- the order of one reveal inside one implementation issue
- a line that works here but does not travel well outside this passage

The extraction agent should ask:

> Is this reusable guidance, or just an accepted choice for this exact scene?

If the answer is "just this scene," treat it as accepted prose beat or `Scene-Specific Correction`, not as a new candidate rule.

## Discarded Draft Wording vs Canon Risk

Do not treat every removed name, object, place, or mechanism as a canon-boundary risk.

Distinguish between:

- a discarded draft phrase
- a provisional noun that might accidentally enter canon
- an actual canon-boundary risk that needs preservation or warning

If the author clarifies that something was only draft wording from a rejected phrasing, mark it as discarded local draft material and do not create a separate issue for it.

## Inputs

Acceptable inputs:

- ChatGPT shared conversation URL
- exported ChatGPT conversation log
- pasted transcript
- selected excerpts from a conversation
- author summary of a session
- attached chat-export PDF

If the agent cannot access a shared URL, it should ask the author for an export, paste, or selected excerpts rather than guessing.

The clean default is that the author attaches or provides the chat log directly, as in a PDF export or pasted transcript, and the extraction agent works from that source.

## Required References

Before extraction, read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/mode_preflight_workflow.md` when the scope is non-trivial or issue logging is likely
3. Relevant canon or style files if the session touches them:
   - `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
   - `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
   - `rules/noir_narration_rules.md`
   - relevant character profiles, relevant location profiles, chapter drafts, scene drafts, outlines, or notes

Apply the drafting-state protocol from `AI_REPO_CONTEXT.md` throughout.

## Existing-Guidance Check

Before presenting a candidate as new, check whether the rule already exists in current repo guidance.

Look first in:

1. `rules/noir_narration_rules.md`
2. relevant character profiles
3. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
4. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
5. relevant chapter outlines or approved local notes for the requested scope
6. relevant case, object, or organisation files if they already exist

The extraction pass should ask:

> Is this actually new, or is this a rediscovery, restatement, refinement, or supporting example of an existing rule?

Possible outcomes:

- `New candidate`
- `Refinement of existing guidance`
- `Existing rule already covers this`
- `Existing rule, but clearer wording was discovered`
- `Existing local pattern already covers this`
- `Possible duplicate; needs validation`
- `Already represented; no issue needed`

The same logic applies to entity surfaces:

- `Existing entity surface already covers this`
- `Existing entity surface, but clearer summary was discovered`
- `New entity candidate`
- `Entity candidate exists only in scaffold form so far`

Do not surface rediscovered guidance as if it were a fresh rule unless there is a meaningful difference.

If the guidance is already present and the session mainly sharpens phrasing, emphasis, ordering, or section clarity, prefer `Refinement of existing guidance` over `New candidate`.

If the repo already contains the guidance in an adequate place and the session does not create a meaningful delta, mark it as `Already represented; no issue needed`.

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
Even a strong candidate may still be only a restatement of a rule that already exists.

Weak extraction signals include:

- polished assistant prose without author approval
- speculative assistant summaries
- newly invented names, artifacts, organisations, or plot mechanics without explicit promotion
- broad thematic claims not grounded in a concrete correction or successful passage
- highly local revision fixes being overstated as project-wide rules
- prose that sounds good but does not produce reusable guidance
- rediscovering an existing rule and presenting it as new without checking the repo

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

These often classify as `Character Guidance`, sometimes with `Global Rule` or `Local Pattern` scope.

### Scene Patterns

Reusable structures that can guide future drafting.

Example:

1. embodied recognition
2. sensory destabilisation
3. gradual environmental return
4. failed professionalism
5. conversational steering

These often classify as `Local Pattern` or `Scaffold Material`, depending on whether they are reusable guidance or a specific chapter movement.

### Scaffolds

Plot directions, sequence shapes, reveal orders, case scaffolds, and chapter movements that are useful to preserve even when they are not yet durable rules.

Examples:

- the opening case should first appear as a treasure-object problem, then widen into mystery
- Chapter 1 should move from office privacy into ritual, recognition, reveal, and only then controlled questioning

These should usually classify as `Scaffold Material`, not `Global Rule`.

### Character Guidance

Bounded character-profile guidance, relationship guidance, or dynamic-specific behaviour discoveries that should not be flattened into general prose rules.

Examples:

- Odette's control should read as survival labour rather than decorative glamour
- Dragon converts embarrassment into procedure

These may later target character profiles, dynamic notes, or chapter-bounded guidance after one-by-one approval.

### Location Guidance

Bounded location-profile guidance, district logic, institution behavior, or recurring place constraints that should not be flattened into general prose rules.

Examples:

- Dragon's office should undermine professionalism through dampness, drafts, clutter, and weak heat
- Toy City should signal preservation pressure, social difference, and repair politics through visible consequences rather than lore explanation
- a recurring location may imply stable geometry, object grouping, approach path, or weather-pressure side that belongs in a location profile
- the prose may establish what can vary in a room and what should stay spatially stable

These may later target location profiles, chapter-bounded notes, or scene-pattern references after one-by-one approval.

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

The first output should usually be a compact extraction triage, not a full analyst report and not direct edits to canon files.

After extraction:

- use `notes/rule_validation_workflow.md` before promoting candidate rules into canon or maintained guidance
- use the character-guidance or location-guidance approval and logging path before updating profile material
- use `notes/scaffold_capture_workflow.md` or a planning/scaffold issue when the extracted item is really scaffold material

If the author says `log that` after reviewing the extraction summary, the agent should not jump straight into canon edits. It should treat that as permission to begin a rule-by-rule validation and logging pass.

Unless the user explicitly asks for direct implementation, the agent should assume that approved extraction findings are meant to be preserved through issues rather than written into canon files immediately.

Issue logging should be selective.

Do not log a new issue just because an item was discussed and validated. If the item is already substantially represented in the repo, prefer one of these outcomes:

- no issue
- a refinement note inside the extraction report
- a follow-up issue only if the repo has a real gap, ambiguity, or placement problem that implementation work still needs to resolve

Before logging an issue from extraction, ask:

- Is this already captured by an existing implementation issue?
- Is this merely accepted wording or a beat for the current scene?
- Is this a scene-specific correction rather than reusable guidance?
- Is this a discarded draft phrase rather than a canon/provisional risk?
- Does this survive as reusable guidance outside the immediate passage?
- Is there a real unresolved repo task?

If no, do not log a new issue.

## Default Output: Compact Triage

The default extraction output should be short and high-signal.

It should usually contain:

- a brief source summary
- `1-3` likely `Global Rule` candidates for the whole story that appear genuinely new or meaningfully refined
- `1-3` likely `Local Pattern` candidates for the current chapter/scene scope that appear genuinely new or meaningfully refined
- `0-3` likely `Character Guidance` candidates when the session materially clarified behavior or dynamic logic
- `0-3` likely `Location Guidance` candidates when the session materially clarified place logic, district behavior, or recurring scene-space function
- `0-3` likely `Case Guidance` candidates when the session materially clarified what the case is, how it should appear, or what remains hidden
- `0-3` likely `Object Guidance` candidates when the session materially clarified what an important object is, appears to be, or pressures in scenes
- `0-3` likely `Organisation Guidance` candidates when the session materially clarified group pressure, cover story, or institutional logic
- `0-3` likely `Scaffold Material` captures when the session produced usable plot or structural direction
- a short `Do Not Promote Yet` section
- a short note if the session is mostly scene-specific rather than rule-heavy
- a short note when the session mostly confirms guidance the repo already has
- a short note when a candidate is better treated as a refinement of existing guidance than as a fresh issue
  - a closing question such as:
    - `Do you want to validate these one by one, log the scaffold items, or both?`

By default, do not lead with:

- large category tables
- long evidence paragraphs
- follow-up issue suggestions
- long continuity-risk sections
- many Scene-Specific Corrections
- prose fragments
- scene-fix lists
- chapter-specific revision planning

The default goal is triage, not completeness.

Evidence in the compact triage should be compressed into one short sentence per candidate.

If a candidate appears to duplicate an existing rule, the compact triage should say so plainly instead of listing it as new.

Example duplicate handling:

- `This appears to restate existing consequence-first narration guidance in `rules/noir_narration_rules.md`, with a cleaner chapter-specific example rather than a new rule.`

Example refinement handling:

- `This looks like a refinement of the existing pink-dragon recognition guidance in `characters/pink_dragon_character_profile.md`, not a separate gap that needs its own issue unless we want a more explicit section.`

Example compression:

- `Author rejected explicit interpretation in favor of consequence, movement, and pause.`
- `Author approved a post-coffee behavioural-similarity beat before the hat/coat reveal.`

## Expanded Output

Use the expanded extraction report only when:

- the author explicitly asks for full detail
- the author explicitly asks to see local corrections
- the author says `log that`
- the session is being turned into structured candidate logging

The expanded report should:

- summarize the source material
- list extracted items by category
- list extracted items by `Type` and `Scope`
- classify the scope of each item before treating it as guidance
- give each item a canon state
- include provenance, such as conversation URL, export filename, date, or author-provided session label
- identify proposed target files
- identify items that require author approval before canon promotion
- stay focused on rule candidates and rule-supporting context

The expanded report should also mark each candidate as one of:

- `New`
- `Refinement of existing guidance`
- `Duplicate of existing guidance`
- `Unclear / needs comparison`

If the session is mostly local revision intelligence, the expanded report should still say that plainly instead of inflating local corrections into a fake rule system.

If the session produced mixed outputs, the expanded report should keep them separated instead of flattening them all into “rules.”

## `Log That` Handoff

If the author responds to an extraction summary with something like:

- `log that`
- `ok log that`
- `turn that into issues`
- `capture those`

the agent should interpret it as:

1. preserve the extracted candidates
2. begin one-by-one validation for rule, local-pattern, and character-guidance candidates
3. preserve scaffold items through the scaffold/logging path rather than pretending they are rules
4. only after each individual candidate passes the relevant approval path, log that approved item in a structured issue or issues
5. avoid direct canon edits unless separately approved

The agent should not treat `log that` as permission to silently write the extracted rules into canon files.

Before creating an issue from a validated candidate, ask:

> Is there a real unresolved repo change here, or is this already represented and simply worth remembering?

Only create the issue when there is a real unresolved repo task.
The agent should also not create candidate-rule issues from the summary alone. Each issue-worthy item must first survive the one-by-one check.

Recommended behavior:

- `Global Rule` and `Local Pattern`
  Present them one by one through `notes/rule_validation_workflow.md`

- `Scene-Specific Correction`
  Exclude them from the default extraction output unless the author explicitly asks to inspect local corrections

After validation, the agent may log the approved candidates as issue-based implementation work, but the later implementation step must still repeat the relevant manual checks before any canon file is changed.

Do not:

- dump whole transcripts into the repo
- promote provisional nouns into canon
- turn local revision advice into project-wide rules without a scope test
- rewrite story files during extraction
- drift into prose extraction or revision planning while in Session Extraction mode
- overwrite existing rules without explaining what changed
- skip rule-by-rule author validation when turning extracted knowledge into canon guidance

## Compact Triage Template

```md
# Session Extraction Triage

## Source

- Link or file:
- Session date:
- Scope requested:

## Summary

Two or three sentences on what the session mainly discovered.

## Likely Global Rule Candidates

- Rule:
  Scope meaning: whole story
  Status:
  Evidence:
  State:

## Likely Local Pattern Candidates For The Current Chapter / Scene

- Pattern:
  Scope meaning: current chapter / scene
  Status:
  Evidence:
  State:

## Likely Character / Location / Entity Candidates

- Character / Location / Case / Object / Organisation:
  Status:
  Evidence:
  Existing surface or new candidate:
  State:

## Already Covered / Likely Duplicate

- Existing guidance:
  Why it seems already covered:

## Do Not Promote Yet

- [item]

## Optional Note

- This session is mostly scene-specific revision guidance.

## Next Step

Do you want to validate these one by one, log the scaffold items, or both?
```

## Expanded Extraction Report Template

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

| Rule | Scope | Status | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Character Behaviour

| Rule | Character | Scope | Status | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Scene Patterns

| Pattern | Scope | Status | State | Evidence | Suggested Target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Anti-Patterns

| Anti-pattern | Scope | Status | Why It Fails | State | Suggested Target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Already Covered / Refinements

| Candidate | Existing Guidance | Status | Why It Is Not New Yet |
| --- | --- | --- | --- |
|  |  |  |  |

## Continuity Risks

| Risk | Location / Evidence | Suggested Handling |
| --- | --- | --- |
|  |  |  |

## Do Not Promote Yet

- 
```

## Target Guidance By Scope

Use scope to constrain where extracted items should go.

- `Global Rule`
  Usual targets: `rules/noir_narration_rules.md`, story bible, prompt pack, durable character or location profiles

- `Local Pattern`
  Usual targets: chapter outlines, character profiles, location profiles, chapter-specific notes, scene-pattern references

- `Scene-Specific Correction`
  Usually out of scope for default Session Extraction output
  inspect only if the author explicitly asks for local corrections

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
Read `README.md`, `AI_REPO_CONTEXT.md`, and `notes/session_extraction_workflow.md`.

Then review this ChatGPT conversation link or exported transcript:

[source here]

Extract reusable Dragon Noir rule knowledge from author corrections, approvals, rejections, and explanations. For every item, first classify scope as `Global Rule`, `Local Pattern`, or `Scene-Specific Correction`, then classify canon state as [EXPLORE], [HOLD], [CANON], or unclear. Check current repo guidance before surfacing it as new, and mark whether it is new, duplicate, or a refinement of something already present. Start with a compact triage summary, not a full analyst report. Focus on rules, patterns, anti-patterns, continuity-risk warnings, and process lessons. Do not drift into prose extraction, revision planning, or issue suggestions unless I explicitly ask for that. Do not edit canon files or story prose unless I approve the extraction report afterward. If I say `log that`, move into rule-by-rule validation and structured candidate logging rather than direct canon edits.
```

For canon promotion after extraction, switch to `notes/rule_validation_workflow.md`.
