# Scaffold Capture Workflow

Provisional workflow for capturing a new plot direction, case shape, chapter scaffold, or sequence idea and deciding what, if anything, belongs in the knowledge base.

This workflow exists because not every useful story discovery begins as a finished draft or a reusable rule. Sometimes the author arrives with a scaffold:

- a plot direction
- a chapter movement
- a mystery shape
- a case/object idea
- a scene sequence
- a structural correction

That material should be preserved cleanly without forcing it straight into canon or flattening it into a rule too early.

## Purpose

Use this workflow when the author wants to:

- capture a new plot direction
- preserve a scaffold for later writing
- turn a structural idea into a durable repo note
- separate provisional story planning from reusable craft knowledge
- derive chapter/scene guidance from a scaffold without over-promoting plot specifics

## Core Rule

The scaffold itself is planning material first.

Do not treat a scaffold as canon just because it is clear, promising, or repeated.

If the scaffold contains durable writing knowledge, extract that separately and classify it correctly.

## Output Layers

When processing a scaffold, separate the result into these layers:

### 1. Scaffold Material

The plot or structural idea itself.

Examples:

- the next Chapter 1 movement
- a possible opening case
- the order of a reveal sequence
- a suspect/object/problem scaffold

Default destination:

- `notes/`
- relevant outline file
- relevant chapter planning note

This layer is usually `[EXPLORE]` or `[HOLD]`, not `[CANON]`.

### 2. Local Guidance

Bounded guidance that applies to a chapter, scene family, or dynamic.

Examples:

- this chapter should delay formal case exposition until after ritual and recognition
- this reveal works best when similarity appears before explicit naming
- Dragon should accept this case for layered practical reasons

Default destination:

- relevant outline
- chapter-specific note
- dynamic-specific planning note

This is usually a `Local Pattern`, not a `Global Rule`.

### 3. Global Knowledge

Reusable craft or story guidance that really does travel beyond the scaffold.

Examples:

- implication should arrive through consequence and object interaction before interpretation
- local recognition scenes should prefer bodily evidence over direct analytical naming

Default destination:

- rule validation flow first
- then canonical guidance files only after approval

This layer must be handled carefully. A scaffold may contain no real global knowledge, and that is fine.

## Processing Steps

### 1. Identify The Scope

Before writing anything down, identify what kind of scaffold this is.

Possible scaffold scopes:

- chapter scaffold
- scene scaffold
- case/object scaffold
- reveal sequence scaffold
- character-dynamic scaffold
- broader plot direction

### 2. Capture The Scaffold Cleanly

Preserve the actual direction in plain language.

The first summary should answer:

- what the scaffold is trying to do
- what part of the story it belongs to
- what sequence or movement it proposes
- what is still intentionally undefined

Do not immediately convert this into abstract writing advice.

### 3. Separate Planning From Knowledge

After the scaffold is captured, classify each worthwhile takeaway as one of:

- `Scaffold Material`
- `Local Pattern`
- `Global Rule`

Use this test:

> Would this still help if the objects, plot nouns, and exact scene changed?

If no, it is scaffold material.

If only within this chapter/scene/dynamic, it is a local pattern.

If it travels across the project, it may be a global rule candidate.

### 4. Check Whether The Knowledge Already Exists

Before treating a takeaway as new, check the current repo guidance:

- `rules/noir_narration_rules.md`
- relevant character and location profiles
- the story bible
- the prompt pack
- relevant outlines and active notes

Classify the result as:

- `New scaffold note`
- `New local pattern`
- `Existing guidance already covers this`
- `Existing guidance, but this scaffold clarifies it`
- `Possible duplicate; validate before adding`

### 5. Store Each Layer In The Right Place

Store the scaffold itself as planning material.

Store local patterns near the chapter, scene, or dynamic they govern.

Route global-rule candidates into `notes/rule_validation_workflow.md` before they are added anywhere authoritative.

## What This Mode Should Produce

The default output should be short and structured.

It should usually include:

- `Scaffold Summary`
- `Scope`
- `State` (`[EXPLORE]`, `[HOLD]`, or `[CANON]` if explicitly promoted)
- `Local Patterns Found`
- `Global Rule Candidates Found`
- `What Stays Provisional`
- `Suggested Repo Target`

## What This Mode Should Not Do

Do not:

- treat a plot direction as canon by default
- flatten scene/chapter logic into whole-project rules too early
- send raw scaffold material straight into the story bible
- skip duplicate checking against existing guidance
- write global rules without rule validation
- confuse “useful for later writing” with “belongs in the knowledge base”

## Relationship To Other Workflows

- Use `notes/writing_workflow.md` when the author wants to draft prose from the scaffold.
- Use `notes/session_extraction_workflow.md` when the source is a transcript/session and the goal is rules extraction.
- Use `notes/rule_validation_workflow.md` when a scaffold produces candidate local/global guidance that should be approved one by one.
- Use `notes/issue_workflow.md` when the author wants the scaffold logged as a GitHub planning/scaffold issue.

## Minimal Agent Prompt

Use this when asking an agent to capture a new plot direction cleanly:

```text
Connect to my repo lewtondoteth/DragonNoir and switch to Scaffold Capture mode.

Follow `notes/scaffold_capture_workflow.md`.

Capture this plot direction or scaffold as provisional planning material first. Separate the scaffold itself from any local patterns or global-rule candidates, check whether those already exist in the repo, and store each result in the correct layer without promoting plot specifics into canon.
```
