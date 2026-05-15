# Profile Pull / Profile Scan Workflow

Provisional workflow for scanning existing prose and extracting durable character-profile, location-profile, dynamic, or spatial guidance from what is already on the page.

This workflow exists for moments when the useful knowledge is already embodied in draft prose rather than in a chat transcript.

## Purpose

Use this workflow when the author wants an agent to read prose and answer questions like:

- what stable character traits are implied here?
- what place logic or spatial characteristics are now clear enough to preserve?
- what should move into a character profile or location profile?
- what in this prose is just local staging, and what is durable guidance?

This is not ordinary critique and not freeform drafting.

It is a profile-focused extraction pass over prose.

You can think of this as a manual profile pull from prose.

## Inputs

Acceptable inputs:

- chapter drafts
- scene drafts
- quoted passages
- assembled prose sequences
- specific location scenes such as office-entry or city-movement scenes

## Required References

Before scanning, read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
4. `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
5. `rules/noir_narration_rules.md`
6. relevant character profiles
7. relevant location profiles
8. relevant chapter, scene, outline, or note files

## What To Look For

When scanning prose, look for durable profile knowledge such as:

- recurring behavior
- repeated conversational habits
- stable emotional logic
- place atmosphere that behaves consistently across scenes
- stable physical features of a recurring location
- geometry or layout assumptions that staging keeps reusing
- recurring objects that belong to the place rather than one isolated beat
- what can vary scene to scene and what should stay spatially stable

## Character vs Location vs Scene Detail

Before surfacing a finding, ask:

1. is this a durable character trait?
2. is this durable location guidance?
3. is this only local scene staging?

Examples:

- `Dragon turns embarrassment into procedure` may be character guidance
- `Dragon's office forces visitors to negotiate around the desk` may be location guidance
- `the cup sat slightly left of the notebook in this paragraph` is just scene staging

## Spatial Characteristic Test

When scanning for place logic, ask:

> Is this merely where something happened in this draft, or is it part of how this location consistently works?

Good profile candidates:

- weather always pressures the office from the window side
- the office is cramped enough that movement through it matters
- Toy City should imply distance, friction, and uneven safety
- the room's clutter can vary, but the desk remains inconvenient

Poor profile candidates:

- one temporary object placement
- one improvised action that does not imply stable layout
- one bit of blocking with no broader place logic

## Output Shape

Start with a compact triage.

Separate findings into:

- likely `Character Guidance`
- likely `Location Guidance`
- likely `Local Pattern`
- `Scene-Specific Detail` that should not be promoted

For each likely character or location item, say whether it appears:

- new
- already represented
- a refinement of existing profile material

## Next Step

After triage:

- use one-by-one approval before changing any profile
- use the candidate logging path if the author wants the item preserved without immediate canon edits
- use `notes/rule_validation_workflow.md` when the finding is really a reusable rule or local pattern rather than profile material

## Do Not

- do not treat all good prose as profile material
- do not flatten scene staging into fake geometry canon
- do not update profiles without explicit approval
- do not override existing profiles without comparing against them
- do not infer new named locations or institutions unless explicitly approved
