# Tools

Small repo-maintenance helpers live here.

## Files

- `generate_repo_manifest.py` — regenerates `notes/repo_manifest.json` and `notes/repo_manifest.md` so agents have a current index of the repo tree, authoritative files, and mode-routing map.
- `setup_repo_hooks.sh` — configures this local checkout to use the tracked `.githooks/` directory.
- `../.githooks/pre-commit` — local Git hook that refreshes and stages the generated manifest files before commits.

## Usage

Refresh the manifest with:

```bash
python3 tools/generate_repo_manifest.py
```

Run this after:

- adding, removing, or renaming files or folders
- changing repo work modes or workflow docs
- changing the top-level structure in a way that affects agent orientation

To make this automatic for local commits, enable the tracked hooks directory:

```bash
sh tools/setup_repo_hooks.sh
```

The generator also records unexpected top-level directories in the manifest maintenance warnings. If a new top-level folder is intentional, update the README and generator structure together; if it is accidental or legacy material, remove or relocate it.
