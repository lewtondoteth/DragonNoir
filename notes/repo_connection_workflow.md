# Repo Connection Workflow

Provisional front-door workflow for AI agents entering the Dragon Noir repository.

This workflow defines what should happen when the author says:

> connect to the repo

or:

> connect to my DragonNoir repo

The purpose is to make the entry point consistent. The agent should connect, scan the repository, orient itself, confirm what kind of work is being requested, and then route into the correct workflow without the author having to restate the whole system every time.

## Entry Trigger

Treat phrases such as these as the same instruction:

- connect to the repo
- connect to my DragonNoir repo
- open DragonNoir
- enter the repo
- load the Dragon Noir workspace

These phrases mean:

1. read the repo bootstrap files
2. understand current context
3. identify the available work modes
4. ask what mode the author wants
5. route into the correct flow

The connection step is orientation, not implementation. The agent should not start rewriting story files, canon files, or notes until the work mode is clear.

## Required Startup Read

On connection, read:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/mode_preflight_workflow.md`

Then briefly scan the current working structure, relevant notes, and current worktree status if needed.

The goal is to be able to say, in effect:

> I have looked at the repo, opened the key guidance, and I know what is available from here.

If the tree has changed or the scope is non-trivial, refresh the repo manifest before mode work:

```bash
python3 tools/generate_repo_manifest.py
```

## What The Agent Should Report After Connecting

After the startup read, the agent should give a short orientation summary that covers:

- this is the Toy Noir Dragon repo
- the active canon/provisional boundaries
- the main current guidance files
- whether there are important uncommitted changes in the working tree
- which work modes are available

The summary should be brief. The purpose is confidence, not a file inventory dump.

## Routing Question

After orienting, the agent should ask what mode the author wants.

The routing question should be simple and concrete, for example:

> I have the repo context loaded. Are we doing Writing, Review, Session Extraction, Profile Pull / Character Scan / Entity Scan / Consistency Scan, Rule Validation, Rule Audit, Scaffold Capture, Canon Promotion, or Issue Work?

If the author already made the mode clear, do not ask again. Route immediately.

## Work Modes

Use these mode names as the standard Dragon Noir roles.

### Writing

Use for drafting, scene revision, prose integration, chapter continuation, structural editing, and implementation-style story work.

Route to:

- `notes/writing_workflow.md`

Writing mode should not jump directly from repo connection into prose generation. It should first retrieve and summarize the active scope context.

### Review

Use for critique, feedback, audit of prose quality, continuity checking, and rule-based read-only assessment.

Route to:

- Review Path in `AI_REPO_CONTEXT.md`

This mode is read-only unless the author explicitly asks for implementation after review.

Review should check not only prose quality but also whether tone, motivations, actions, and location logic stay consistent with the current canon files. If it finds a likely clash, the default path is to identify it, ask any needed clarification one question at a time, and log an issue rather than silently fixing it.

### Session Extraction

Use for reading ChatGPT share links, exports, transcripts, notes, or excerpts and pulling out reusable knowledge from corrections, approvals, rejections, and comments.

Route to:

- `notes/session_extraction_workflow.md`

This is a separate analysis role, not a continuation of Writing mode. The normal flow is:

1. connect to the repo
2. choose `Session Extraction`
3. provide a chat log, export, pasted transcript, or selected excerpts
4. let the extraction agent analyze the session after the fact
5. validate worthwhile findings one by one
6. log approved candidates as issues unless the author explicitly asks for direct implementation

This separation exists so drafting interests and extraction interests do not get mixed together.

### Profile Pull

Use for scanning existing prose and extracting durable character-profile, location-profile, case-profile, object-profile, organisation-profile, dynamic, or spatial guidance from the draft itself.

Route to:

- `notes/profile_scan_workflow.md`

This mode is for reading what the prose already implies and deciding what belongs in profiles or bounded guidance, especially when useful spatial characteristics or stable place logic have emerged through drafting.

The default preservation path here is the same:

1. scan the prose
2. validate worthwhile profile findings one by one
3. log approved candidates as issues
4. implement later only if the author explicitly asks

Treat these phrases as the same mode:

- `Profile Pull`
- `Profile Scan`
- `Character Scan`
- `Entity Scan`
- `Consistency Scan`
- `scan this prose for profile updates`
- `scan this prose for character consistency`
- `scan this prose for entity updates`
- `pull profile guidance from this chapter`

### Rule Validation

Use when candidate rules have been extracted and the author wants to approve them one at a time before they are written into canon or maintained guidance.

Route to:

- `notes/rule_validation_workflow.md`

### Rule Audit

Use when the author wants to go through the current existing rule set one rule at a time and decide whether to keep, revise, split, merge, move, demote, or remove each rule.

Route to:

- Existing Rule Audit section in `notes/rule_validation_workflow.md`

### Scaffold Capture

Use when the author arrives with a plot direction, sequence scaffold, case shape, chapter movement, or structural idea that should be preserved and possibly distilled into reusable knowledge.

Route to:

- `notes/scaffold_capture_workflow.md`

This mode captures planning material first, then separates out any local patterns or global-rule candidates without promoting plot specifics into canon by accident.

### Canon Promotion

Use when material is currently provisional, exploratory, or hold-state and the author wants to explicitly promote it into canon files.

Route to:

- canon-promotion logic in `notes/issue_workflow.md`
- relevant target canon files

Canon promotion must be explicit. Do not infer it from enthusiasm or repetition.

### Issue Work

Use for logging issues, implementing issues, reviewing issue scope, or closing issue-driven tasks.

Route to:

- `notes/issue_workflow.md`

## Mode Selection Rule

If the author gives only the connection command and nothing else, the agent should orient first and then ask which mode applies.

If the author gives the connection command plus a clear task, the agent should:

1. connect
2. load the bootstrap files
3. identify the implied mode
4. state the mode briefly
5. continue into that flow

Example:

- `connect to my DragonNoir repo and review this chapter`
  - connect
  - route to Review

- `connect to the repo and extract rules from this chat`
  - connect
  - route to Session Extraction

- `connect to the repo and extract from this chat log`
  - connect
  - route to Session Extraction

- `connect to DragonNoir and audit the current rules`
  - connect
  - route to Rule Audit

- `connect to DragonNoir and capture this Chapter 1 scaffold`
  - connect
  - route to Scaffold Capture

- `connect to DragonNoir and scan this chapter for profile updates`
  - connect
  - route to Profile Pull

- `connect to DragonNoir and run a consistency scan on this chapter`
  - connect
  - route to Profile Pull

## Safety Rules

During connection and routing:

- do not treat exploratory nouns as canon
- do not start editing before the mode is clear
- do not skip `README.md` and `AI_REPO_CONTEXT.md`
- do not route Review into Writing unless the author explicitly changes modes
- do not route Session Extraction straight into canon edits without Rule Validation
- do not treat Session Extraction as live drafting or prose generation
- do not treat Profile Pull as ordinary prose critique or as permission to silently update profiles
- do not route Rule Validation into canon changes without rule-by-rule approval
- do not route Scaffold Capture straight into canon promotion without explicit approval

## Minimal Agent Prompt

Use this when asking an agent to enter the repo cleanly:

```text
Connect to my DragonNoir repo.

Read `README.md` and `AI_REPO_CONTEXT.md`, orient yourself to the repo, summarize the current context briefly, and tell me which work modes are available from here:
- Writing
- Review
- Session Extraction
- Profile Pull / Character Scan / Entity Scan / Consistency Scan
- Rule Validation
- Rule Audit
- Scaffold Capture
- Canon Promotion
- Issue Work

If I have already made the task clear, route directly into the correct workflow. Otherwise, ask me which mode we are in.
```
