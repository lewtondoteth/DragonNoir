# Repo Manifest

Generated helper index for Dragon Noir agents.

- Generated at: `2026-05-15T19:28:38+00:00`

## Authoritative Reference

- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- `rules/noir_narration_rules.md`
- `characters/pink_dragon_character_profile.md`
- `locations/Toy_City_location_profile.md`
- `locations/Dragon_Office_location_profile.md`
- `cases/README.md`
- `objects/README.md`
- `organisations/README.md`

## Modes

### Writing

- Route: `notes/writing_workflow.md`
- Default action: retrieve scope context, check open issues, then draft
- Aliases: `draft`, `write`, `continue chapter`, `scene revision`

### Review

- Route: `AI_REPO_CONTEXT.md#review-path`
- Default action: read-only review, ask clarifications one at a time if needed, then log issues
- Aliases: `review`, `critique`, `audit prose`, `feedback`

### Session Extraction

- Route: `notes/session_extraction_workflow.md`
- Default action: extract, validate one by one, then log issues by default
- Aliases: `extract from chat`, `extract from transcript`, `chat extraction`

### Profile Pull

- Route: `notes/profile_scan_workflow.md`
- Default action: scan prose, identify entity guidance or conflicts, validate or clarify, then log issues by default
- Aliases: `profile scan`, `character scan`, `entity scan`, `scan this prose for profile updates`

### Consistency Scan

- Route: `notes/profile_scan_workflow.md`
- Default action: check prose against rules, profiles, and location logic, then log issues by default
- Aliases: `consistency scan`, `scan this prose for character consistency`

### Rule Validation

- Route: `notes/rule_validation_workflow.md`
- Default action: validate candidates one at a time
- Aliases: `validate rules`, `rule by rule`

### Rule Audit

- Route: `notes/rule_validation_workflow.md#existing-rule-audit`
- Default action: audit existing rules one by one
- Aliases: `audit rules`, `review current rules`

### Scaffold Capture

- Route: `notes/scaffold_capture_workflow.md`
- Default action: separate scaffold, local guidance, and global knowledge, then log issues by default when preserving
- Aliases: `capture scaffold`, `capture plot direction`

### Canon Promotion

- Route: `notes/issue_workflow.md#canon-promotion-issue-template`
- Default action: promote explicitly approved material only
- Aliases: `promote to canon`, `canonise`

### Issue Work

- Route: `notes/issue_workflow.md`
- Default action: use issue workflow and acceptance criteria
- Aliases: `log issue`, `implement issue`, `close issue`

## Recommended Issue Labels

### mode

- `mode:writing`
- `mode:review`
- `mode:session-extraction`
- `mode:profile-scan`
- `mode:scaffold-capture`
- `mode:issue-work`

### type

- `type:implementation`
- `type:review`
- `type:scaffold`
- `type:canon-promotion`
- `type:candidate-rule`
- `type:candidate-character`
- `type:candidate-location`
- `type:candidate-case`
- `type:candidate-object`
- `type:candidate-organisation`
- `type:consistency-fix`

### scope_examples

- `scope:chapter-1`
- `scope:dragon-office`
- `scope:toy-city`
- `scope:odette`

## Top-Level Files

### cases

- `cases/README.md`

### chapters

- `chapters/README.md`
- `chapters/chapter_01_opening.md`

### characters

- `characters/pink_dragon_character_profile.md`

### discarded_or_experimental

- `discarded_or_experimental/README.md`

### locations

- `locations/Dragon_Office_location_profile.md`
- `locations/README.md`
- `locations/Toy_City_location_profile.md`

### notes

- `notes/README.md`
- `notes/development_options.md`
- `notes/issue_workflow.md`
- `notes/mode_preflight_workflow.md`
- `notes/opening_case_music_box_scaffold.md`
- `notes/profile_scan_workflow.md`
- `notes/repo_connection_workflow.md`
- `notes/repo_manifest.json`
- `notes/repo_manifest.md`
- `notes/rule_validation_workflow.md`
- `notes/scaffold_capture_workflow.md`
- `notes/session_extraction_workflow.md`
- `notes/writing_workflow.md`

### objects

- `objects/README.md`

### outlines

- `outlines/chapter_01_narrative_beats.md`

### organisations

- `organisations/README.md`

### rules

- `rules/noir_narration_rules.md`

### scenes

- `scenes/README.md`
- `scenes/chapter_01_office_entry_coffee_ritual_draft.md`

### story_bible

- `story_bible/README.md`
- `story_bible/Toy_Noir_Dragon_AI_Prompt_Pack.md`
- `story_bible/Toy_Noir_Dragon_Standalone_Story_Bible.md`

### tools

- `tools/README.md`
- `tools/generate_repo_manifest.py`
