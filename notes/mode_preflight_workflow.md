# Mode Preflight Workflow

Shared preflight workflow for all Dragon Noir repo modes.

This workflow exists to reduce repeated setup work and make the mode system scale as the repo grows.

Use it after repo connection and before entering:

- `Writing`
- `Review`
- `Session Extraction`
- `Profile Pull`
- `Character Scan`
- `Consistency Scan`
- `Rule Validation`
- `Rule Audit`
- `Scaffold Capture`
- `Canon Promotion`
- `Issue Work`

## Purpose

The preflight should do the repeated mechanical work once so each downstream workflow can stay focused.

Its job is to:

1. refresh the repo manifest if needed
2. load the bootstrap context
3. identify the requested mode and scope
4. gather the minimum relevant files
5. check for already-open issues that match the scope
6. produce a short orientation summary before the mode-specific work begins

## Manifest Refresh

Before mode-specific work, refresh `notes/repo_manifest.json` and `notes/repo_manifest.md` if:

- the manifest does not exist
- the tree has changed
- a major file or folder was added, removed, or renamed
- the workflow docs changed in a way that affects routing

Preferred command:

```bash
python3 tools/generate_repo_manifest.py
```

The manifest should be treated as a helper index, not as canon.

For local commits, `.githooks/pre-commit` can refresh and stage the manifest automatically when `git config core.hooksPath .githooks` has been set.

If the manifest reports unexpected top-level directories, pause before treating them as source material. Either document them in the approved structure or remove/relocate them if they are accidental legacy material.

## Shared Inputs

Always load:

1. `README.md`
2. `AI_REPO_CONTEXT.md`
3. `notes/repo_manifest.json`

Then load the mode-specific workflow file.

## Shared Open-Issue Check

Before proposing new issue logging in any mode, check whether an open GitHub issue already tracks the same scope, conflict, guidance item, or scaffold.

Modes that should always do this:

- `Writing`
- `Review`
- `Session Extraction`
- `Profile Pull`
- `Character Scan`
- `Consistency Scan`
- `Scaffold Capture`

If an open issue already exists:

- mention it
- avoid creating a duplicate
- continue with the workflow using the existing issue as the preservation or repair path

## Shared Question Rule

If clarification is needed before an issue can be framed correctly or a candidate can be validated:

1. ask one question at a time
2. wait for the answer
3. restate the corrected understanding if needed
4. only then log the issue or continue the approval flow

## Mode-Specific Output

The preflight summary should be short and mode-aware.

It should usually include:

- active scope
- authoritative files loaded
- nearby provisional or experimental material to watch
- whether matching open issues already exist
- what the next step in this mode will be

Example:

> I refreshed the manifest, loaded the Chapter 1 draft, outline, Dragon's office profile, and current narration rules. There is one open issue already tracking the office-layout inconsistency, so I’ll reference that instead of logging a duplicate. Next step: run the requested consistency scan.

## Do Not

- do not dump the whole manifest into the conversation
- do not load every repo file when the scope is narrow
- do not skip the open-issue check in logging-heavy modes
- do not let preflight become a second full review
