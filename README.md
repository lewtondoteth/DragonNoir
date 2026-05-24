# Dragon Noir

This repository contains the standalone Toy Noir Dragon book project.

It is now dedicated to the noir continuity only. The family Dragon project remains in the old `Dragon-Stories` repository history and should not be used as guidance here unless explicitly provided again for comparison or adaptation.

## AI / Agent Context

AI assistants and coding agents should read:

1. `../ElectricMonk/AGENTS.md`
2. `README.md`
3. `AI_REPO_CONTEXT.md`

`../ElectricMonk/` contains the shared workflow machinery, also called the Monk. This repository contains the Toy Noir Dragon story content, canon, style, prose, and project-specific scope rules.

`AGENTS.md` contains the short bootstrap instruction that links ElectricMonk to this private story repo.

## Author Workflow

The normal creative workflow is issue-led integration:

1. Draft, brainstorm, revise, or explore prose in a separate AI chat.
2. When the author is happy with a result, log a scoped GitHub issue for the part that should enter this repository.
3. Use the issue as the handoff between exploratory writing and repo implementation.
4. The repo-connected agent implements only the scoped issue material, preserving canon/provisional boundaries.
5. Extraction, review, profile-pull, scaffold-capture, and rule-validation work should normally preserve approved findings through issues unless the author explicitly asks for direct repo implementation.

This repository is therefore the controlled continuity and integration layer, not the scratchpad for every exploratory draft.

## Authoritative Reference

Use this hierarchy when deciding what an AI agent may rely on:

| Level | Meaning | Current Files |
| --- | --- | --- |
| Canon / authoritative guidance | Stable story, tone, character, narration, and world guidance. | `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`; `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`; `rules/noir_narration_rules.md`; `characters/dragon_character_profile.md`; `characters/pink_dragon_character_profile.md`; `locations/Toy_City_location_profile.md`; `locations/Dragon_Office_location_profile.md`; `locations/mercer_street_corner_shop_location_profile.md`; `locations/Harrow_and_Vale_location_profile.md` |
| Active working guidance | Stable enough to guide current drafting, while preserving stated unknowns. | `cases/opening_music_box_case_profile.md`; `objects/music_box_object_profile.md`; `organisations/commissioning_party_profile.md`; `characters/outside_professional_thief_character_profile.md`; `notes/clockwork_orchestra_story_direction_scaffold.md` for the approved early-case path only |
| Provisional planning | Useful planning, not fixed canon unless explicitly promoted. | `notes/opening_case_music_box_scaffold.md`; later-novel material in `notes/clockwork_orchestra_story_direction_scaffold.md` |
| Experimental / retired | Not active guidance unless explicitly revived. | `scenes/chapter_01_office_entry_coffee_ritual_draft.md`; `notes/development_options.md`; `discarded_or_experimental/` |

## File Index

```text
DragonNoir/
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── candidate_guidance.md
│       ├── canon_promotion.md
│       ├── config.yml
│       ├── follow_up.md
│       ├── implementation.md
│       ├── long_session_capture.md
│       ├── planning_scaffold.md
│       └── review_consistency.md
├── .githooks/
│   └── pre-commit
├── .gitignore
├── AGENTS.md
├── AI_REPO_CONTEXT.md
├── README.md
├── cases/
│   ├── README.md
│   └── opening_music_box_case_profile.md
├── chapters/
│   ├── README.md
│   ├── chapter_01.md
│   └── chapter_02.md
├── characters/
│   ├── README.md
│   ├── dragon_character_profile.md
│   ├── outside_professional_thief_character_profile.md
│   └── pink_dragon_character_profile.md
├── discarded_or_experimental/
│   └── README.md
├── locations/
│   ├── README.md
│   ├── Dragon_Office_location_profile.md
│   ├── Harrow_and_Vale_location_profile.md
│   ├── mercer_street_corner_shop_location_profile.md
│   └── Toy_City_location_profile.md
├── objects/
│   ├── README.md
│   └── music_box_object_profile.md
├── notes/
│   ├── README.md
│   ├── clockwork_orchestra_story_direction_scaffold.md
│   ├── development_options.md
│   ├── opening_case_music_box_scaffold.md
│   ├── repo_manifest.json
│   └── repo_manifest.md
├── outlines/
│   ├── README.md
│   └── chapter_01_narrative_beats.md
├── organisations/
│   ├── README.md
│   └── commissioning_party_profile.md
├── rules/
│   ├── README.md
│   └── noir_narration_rules.md
├── scenes/
│   ├── README.md
│   └── chapter_01_office_entry_coffee_ritual_draft.md
├── story_bible/
│   ├── README.md
│   ├── Toy_Noir_Dragon_AI_Prompt_Pack.md
│   └── Toy_Noir_Dragon_Standalone_Story_Bible.md
```

ElectricMonk files live in the sibling repo `../ElectricMonk/`.

## Working Structure

- `chapters/` — canonical or assembled chapter drafts
- `cases/` — canonical case profiles and bounded case-guidance notes
- `scenes/` — scene drafts, fragments, and scene-level experiments
- `outlines/` — chapter architecture, narrative beats, and pacing references
- `characters/` — canonical character profiles and expanded continuity notes
- `locations/` — canonical location profiles and expanded place-continuity notes
- `objects/` — canonical object profiles and bounded object-guidance notes
- `organisations/` — canonical organisation profiles and bounded organisation-guidance notes
- `rules/` — canonical practical writing rules discovered during drafting
- `discarded_or_experimental/` — retired alternatives and preserved non-canonical material
- `notes/` — planning notes, continuity tracking, mystery structure, and revision notes
- `story_bible/` — authoritative noir project bible and prompt pack
- `../ElectricMonk/` — ElectricMonk shared agent workflow machinery and maintenance tools

## Chapter 1 Workflow

- Canonical current draft: `chapters/chapter_01.md`
- Canonical pacing reference: `outlines/chapter_01_narrative_beats.md`
- Current experimental scene sandbox: `scenes/chapter_01_office_entry_coffee_ritual_draft.md`
- Practical narration rules: `rules/noir_narration_rules.md`
- Opening-case scaffold: `notes/opening_case_music_box_scaffold.md`
- Issue workflow: `../ElectricMonk/notes/issue_workflow.md`

Keep canonical prose, experimental scene drafts, and structural outlines separate while drafting.

## Chapter Status

Use this table to understand what each major story artifact is for before editing or reviewing it.

| Item | File | Status | Use for | Notes |
| --- | --- | --- | --- | --- |
| Chapter 1 | `chapters/chapter_01.md` | Active canonical draft | Main Chapter 1 prose | Treat as the current assembled chapter unless the user says otherwise; currently reaches the auction-catalogue case reveal and PI/property-evaluator exchange. |
| Chapter 2 | `chapters/chapter_02.md` | Active canonical draft | Main Chapter 2 prose | Opens with legal formalities and Odette's departure, then follows Dragon through the rain, alley/tin-soldier beat, Mercer Street shop/expense-phone sequence, cab ride, auction-house police-scene arrival, Harrow & Vale threshold entry, and Dragon's initial negotiation to look around. |
| Chapter 1 narrative beats | `outlines/chapter_01_narrative_beats.md` | Active canonical structure | Pacing, sequence, and scene-function reference | Use to check whether new prose still follows the intended opening movement. |
| Office-entry coffee ritual | `scenes/chapter_01_office_entry_coffee_ritual_draft.md` | Experimental scene study | Texture, pacing, and possible integration material | Do not treat as canonical prose unless integrated into the active chapter. |
| Clockwork orchestra story-direction scaffold | `notes/clockwork_orchestra_story_direction_scaffold.md` | Active early-case guidance / provisional wider planning | Current Chapters 1-4 guidance and wider story-direction reference | Use for the approved early case path through Chapter 4; treat later novel movement in the same file as provisional. |
| Opening-case music box scaffold | `notes/opening_case_music_box_scaffold.md` | Provisional planning | Possible opening-case shape | Not fixed canon; promote only by explicit user request or canon-promotion issue. |
| Opening music box case profile | `cases/opening_music_box_case_profile.md` | Active working case profile | Current bounded opening-case logic | Stable enough to guide drafting while keeping the deeper purpose and hidden party morally undefined. |
| Music box object profile | `objects/music_box_object_profile.md` | Active working object profile | Current bounded object logic | Use for what the music box outwardly is and what remains intentionally undefined. |
| Commissioning party profile | `organisations/commissioning_party_profile.md` | Provisional organisation profile | Hidden-party pressure logic | Preserve the hidden party's function without naming or morally fixing them too early. |
| Outside professional thief profile | `characters/outside_professional_thief_character_profile.md` | Provisional character profile | Bounded case-function character logic | Preserve the thief's role in the case without overbuilding them too early. |
| Development options | `notes/development_options.md` | Retired/exploratory notes | Backup ideas and comparison material | Not active canon unless explicitly revived. |

When adding, removing, renaming, or changing the status of a major chapter, scene, outline, or planning artifact, update this table in the same change.

## Current Active Drafts

- `chapters/chapter_01.md` — canonical current Chapter 1 draft. Contains the rain/city opening, Dragon's trifle-hangover state, doorway reveal, office-entry transition, coffee sequence, layered recognition progression, auction-catalogue music-box reveal, Tonight realization, and PI/property-evaluator exchange.
- `chapters/chapter_02.md` — canonical current Chapter 2 draft. Contains the legal formalities, rate agreement, Odette's quiet departure, Dragon leaving through the rain and alley, the tin-soldier beat, the Mercer Street shop/expense-phone sequence, the cab ride to Harrow & Vale, the auction-house exterior police scene with Detective Goldfoot, Dragon's threshold exchange with the nutcracker servant, and the opening negotiation that gets him permission to look around.

## Scene Studies

- `scenes/chapter_01_office_entry_coffee_ritual_draft.md` — experimental office-entry and coffee material. Retained as a scene-study sandbox; do not treat as canonical prose unless integrated into `chapters/chapter_01.md`.

## Outlines And Notes

- `outlines/chapter_01_narrative_beats.md` — canonical Chapter 1 pacing and architecture reference.
- `locations/Toy_City_location_profile.md` — canonical setting profile for Toy City atmosphere, scale, and city logic.
- `locations/Dragon_Office_location_profile.md` — canonical location profile for Dragon's office as recurring scene space.
- `locations/Harrow_and_Vale_location_profile.md` — bounded canonical location profile for Harrow & Vale as the opening case's auction-house institution and threshold exterior.
- `locations/mercer_street_corner_shop_location_profile.md` — bounded canonical location profile for Mercer Street and the unnamed corner shop from Chapter 2.
- `cases/README.md` — guidance for how case profiles should be created and maintained.
- `cases/opening_music_box_case_profile.md` — current bounded opening-case profile for the missing music box case.
- `objects/README.md` — guidance for how object profiles should be created and maintained.
- `objects/music_box_object_profile.md` — current bounded object profile for the music box.
- `organisations/README.md` — guidance for how organisation profiles should be created and maintained.
- `organisations/commissioning_party_profile.md` — current bounded profile for the hidden party behind the theft job.
- `characters/README.md` — guidance for how character profiles should be created and maintained.
- `characters/dragon_character_profile.md` — canonical operational character profile for Dragon's recurring behaviour, local social position, transactional habits, and smoke/fire habit translation.
- `characters/outside_professional_thief_character_profile.md` — current bounded profile for the outside professional thief used in the opening case.
- `outlines/README.md` — guidance for structural references and chapter beat maps.
- `notes/clockwork_orchestra_story_direction_scaffold.md` — current mixed-status story-direction scaffold: approved early case guidance through Chapter 4, with wider novel direction still provisional.
- `notes/repo_manifest.json` — generated machine-readable repo index for agent orientation.
- `notes/repo_manifest.md` — generated human-readable repo index for agent orientation.
- `notes/opening_case_music_box_scaffold.md` — exploratory stolen music box opening-case scaffold. Not fixed canon.
- `notes/development_options.md` — retired, backup, and exploratory ideas. Not active canon unless explicitly revived.
- `rules/README.md` — guidance for maintained writing rules and the rule-validation flow.
- `../ElectricMonk/notes/` — Monk writing, review, extraction, issue, preflight, and connection workflows.
- `../ElectricMonk/tools/generate_repo_manifest.py` — Monk manifest generator.
- `.githooks/pre-commit` — local hook that calls the shared manifest generator and stages generated repo manifests before commits when `core.hooksPath` is set to `.githooks`.
- `.github/ISSUE_TEMPLATE/` — GitHub UI issue templates matching the repo issue workflow.

## Repo Upkeep

When adding, removing, renaming, or moving files, update the relevant README or file index in the same change.

The repo manifest is generated from the current tree. Refresh it with:

```bash
python3 ../ElectricMonk/tools/generate_repo_manifest.py .
```

For automatic manifest refresh on commit, this repo includes `.githooks/pre-commit`. Enable it locally with:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

The hook calls the Monk manifest generator from `../ElectricMonk/`, regenerates `notes/repo_manifest.json` and `notes/repo_manifest.md`, and stages them during commit. If a new top-level folder appears outside the approved structure, the manifest records a maintenance warning so the structure can be cleaned up or documented.

## Issue Workflow

Use GitHub issues as the handoff layer between exploratory development, implementation, and review.

Issue workflow reference:

- `../ElectricMonk/notes/issue_workflow.md`

When asking an AI agent to "log a ticket", "log an issue", "create an issue", or "make a ticket", the agent should create a GitHub issue using the appropriate template and should not edit repository files unless implementation is separately requested.

If the issue comes from a long writing session, chat transcript, or exported conversation, use the Long Session Capture template and the shared rules in `../ElectricMonk/notes/issue_workflow.md` first unless a Session Extraction summary is already attached or the issue explicitly says extraction is not needed.

For `Session Extraction` and `Profile Pull`, the default preservation path is:

1. extract and classify findings
2. validate them one by one
3. log the approved result as the appropriate issue type

Do not treat extraction approval by itself as permission to directly update canon files unless the user explicitly switches into implementation or direct canon-update work.

When extraction or scaffold work surfaces durable entity information, the agent should decide whether it belongs to:

- an existing character profile
- an existing location profile
- an existing case profile
- an existing object profile
- an existing organisation profile
- or a new candidate issue to establish that entity cleanly

The goal is to let repeated drafting and extraction gradually build these canon surfaces out indirectly instead of relying on one big manual worldbuilding pass.

Before logging any new issue in Review, Session Extraction, Profile Pull, Character Scan, Consistency Scan, Writing follow-up logging, or Scaffold Capture, check whether the same scope is already tracked by an open issue and reuse it instead of creating a duplicate.

Implementation agents should treat issues as scoped instructions, not permission to broadly rewrite. Review issues use the read-only AI Review Path. Planning/scaffold issues stay provisional unless the issue explicitly says to promote material into canon.

When logging a new issue, use this repo's `.github/ISSUE_TEMPLATE/` templates and the shared rules in `../ElectricMonk/notes/issue_workflow.md` for implementation, review, planning/scaffold, canon promotion, and follow-up issues.

Before closing an implementation issue, check the acceptance criteria in `../ElectricMonk/notes/issue_workflow.md`, including scope control, canon/provisional boundaries, README/path updates, prose style, character continuity, post-implementation style/flow conflicts, and `git diff --check`.

When implementing an issue, the agent should not jump straight into editing. It should enter the `Implementation Wizard` from `../ElectricMonk/notes/issue_workflow.md`, show the proposed changes one by one, and get approval before each change is made.

If the scoped work is complete but a criterion or style/flow check exposes a real out-of-scope problem, the agent should allow the implementation through and create a follow-up issue explaining what is wrong and how it might be resolved.

## Session Extraction Flow

Use `Session Extraction` as a separate repo role after a drafting chat is finished.

The intended flow is:

1. have the drafting conversation elsewhere
2. provide the chat log, export, transcript, or attached PDF to the repo-connected agent
3. switch into `Session Extraction`
4. let the extraction agent analyze the session for durable knowledge
5. validate any worthwhile findings one by one
6. log approved candidates as issues unless direct implementation is explicitly requested

This includes entity-growth work:

- enrich an existing character, case, object, or organisation surface when the session adds durable information
- or log the right issue to establish that entity if it does not yet have a canon surface

This keeps prose generation and post-writing extraction as distinct activities with different goals.

## Writing Connection Flow

When the author connects to write, agents should not open with a long context report.

The normal writing startup should be compact:

1. confirm the active draft or scene
2. give a short cue from the last saved prose
3. check whether open prose/writing issues contain author-facing draft progress beyond the saved file
4. mention only the most relevant current constraint or provisional forward context, if useful
5. ask what the author wants to write, continue, or change next

Detailed canon, workflow, and file summaries should stay internal unless the author asks for them or a canon/provisional decision is needed.

Before reporting a prose file's last paragraph, latest prose, current endpoint, or end of file, verify the actual EOF. A partial connector fetch or ranged read can end on a complete-looking paragraph without reaching the file end. Continue fetching until EOF is confirmed, or use a file-end read such as `tail` when local access is available.

If open issues preserve prose that has not yet been implemented into the repo, Writing mode may use that material as provisional `Forward Draft Context` so drafting can continue from the author's current working position. This does not make the issue material canon and does not replace later issue processing.

Only actual visible prose can be used as `Forward Draft Context`. Issue summaries, beat lists, remembered session descriptions, and references to unavailable transcripts are not draft text. If an issue points to a transcript, export, PDF, canvas, or earlier chat that is not available in the current session, the agent must say so, compare against the saved draft, and ask for the source prose before reconstructing, logging, or integrating it.

When the author gives a concrete prose instruction such as "replace this," "write this beat," "continue from here," or "revise this passage," the agent should handle the prose request before switching into craft analysis, design interrogation, or issue capture. Do not turn a requested replacement into abstract style lessons unless the author asks for that analysis.

For prose implementation, agents must separate exact wording from beat summaries. Exact visible prose may be copied or lightly stitched; beat summaries require either the source prose or explicit user approval to reconstruct. Reconstructed prose must not be described as restored, recovered, agreed, or preserved.

Visible prose must also be source-classified. Pasted material in review, audit, complaint, or "what went wrong" conversations is a diagnostic excerpt, not approved source prose, unless the author explicitly says to use that exact wording.

Before logging any issue about missing, duplicate, accidental, or conflicting prose, check the current saved file and identify the visible passage or absence. Do not create restoration or cleanup issues from issue metadata alone.

When logging follow-up material after using `Forward Draft Context`, log only the new delta from the current session. Do not duplicate prose, guidance, or scaffold material already present in the saved file or open issues.

During live drafting, if the author says a line or beat feels wrong without knowing why, the writing agent should help diagnose the issue with a few concrete possibilities instead of forcing an immediate explanation. Confirmed diagnoses can later be captured as style, pacing, character, or local-pattern guidance.

After logging or preserving writing-session material, the agent should notice unresolved design choices and offer to go through them one by one. The goal is to capture why rejected options failed and why chosen versions worked, without automatically turning every answer into canon.

After a design choice is unpacked, the agent may offer to log that specific clarified lesson as a new scoped delta. It should not re-log the original prose or already-preserved session material.

## Profile Pull Flow

Use `Profile Pull` when the useful profile knowledge is already embodied in prose and should be extracted from the draft itself rather than from a chat export.

This mode also covers `Character Scan` work: reading prose to extract durable character guidance and to check for clashes against the current character or location profiles.

`Consistency Scan` is an accepted alias when the main goal is to compare prose against the current rules, character profiles, and location profiles and then log any needed fix issues.

This mode may also identify durable case, object, or organisation information already embodied in the prose and route it into the right entity surface or issue path.

The intended flow is:

1. provide the prose, scene, chapter, or passage
2. switch into `Profile Pull`
3. let the agent separate durable profile guidance from local scene staging
4. validate any character-profile, location-profile, or spatial-guidance findings one by one
5. log approved profile candidates as issues unless direct implementation is explicitly requested
6. if the scan finds a clash or inconsistency, identify it clearly, ask any needed clarification questions one at a time, and log a fix issue unless direct implementation is explicitly requested

## Shared Mode Preflight

Use `../ElectricMonk/notes/mode_preflight_workflow.md` before mode-specific work when the scope is non-trivial, the repo tree has changed, or issue dedupe matters.

The preflight should:

1. refresh the repo manifest with `python3 ../ElectricMonk/tools/generate_repo_manifest.py .` when needed
2. load the minimum relevant files for the current scope
3. check for already-open matching issues
4. give a short mode-specific orientation summary before proceeding

## Drafting-State Protocol

Use `[EXPLORE]`, `[HOLD]`, and `[CANON]` to prevent exploratory drafting material from becoming accidental continuity.

Before issue logging, file updates, lore updates, PRs, or summaries that may become handoff material, verify what has actually been approved as canon. If uncertain, generalise the material and avoid promoting provisional names, organisations, artifacts, case terms, or plot mechanics.

## Canonical vs Experimental

- Canonical: story bible, narration rules, character profiles, location profiles, active chapter drafts, and active outline references.
- Canonical entity surfaces may also include case profiles, object profiles, and organisation profiles once they are established.
- Development: notes and opening-case scaffolds that preserve possibilities without locking plot.
- Experimental: scene sandboxes and pacing studies.
- Retired: discarded or backup ideas preserved for later comparison or revival.

## AI Review Path

When asking an AI agent to review, critique, assess, audit, or give feedback, the agent should use a read-only review path.

Review mode means:

- do not edit story files
- do not resolve issues directly
- compare the requested material against the story bible, prompt pack, narration rules, character profiles, location profiles, and relevant outlines/notes
- log detailed issues with reasons and suggested resolution directions

Review should focus especially on:

- pacing and feel of the prose
- whether the passage matches Dragon's first-person noir voice
- whether the tone stays internally consistent across the passage
- consequence-first narration instead of flat stage directions
- implication-heavy emotional movement
- toy-world play-as-reality logic
- character consistency, motives, and action logic against the current character files
- location consistency and stable spatial logic against the current location files
- canon/provisional boundaries
- factual continuity inside the draft
- scene function and structural flow

An issue report should explain where the problem appears, why it conflicts with the repo's rules or story logic, how it affects pacing/feel/continuity/character, and what kind of revision would resolve it.

When review uncovers a likely conflict, gap, or unresolved inconsistency, the normal repair path is:

1. identify the issue clearly
2. ask any needed clarification questions one at a time
3. allow correction before locking the diagnosis
4. log the issue for later implementation unless the user explicitly asks to fix it now

Agents should not rewrite the passage during review unless the user explicitly asks for implementation after the review.

## Active Canon

The active canon is Dragon, the pink dragon, Toy City, narration style, repair logic, treasure instinct, rain logic, play-as-reality toy ontology, and the emotional/thematic dynamics between the two dragons.

The exact case, mystery engine, artifact, antagonist, and ending structure are provisional until deliberately promoted into the story bible.

Retired/provisional noir plot material, including the Ember-Stone, Patchwork Guardian, wind-up mouse courier, and related fixed-plot machinery, belongs in development notes and should not be treated as active canon unless explicitly revived.
