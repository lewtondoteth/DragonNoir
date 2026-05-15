# Tools

Small repo-maintenance helpers live here.

## Files

- `generate_repo_manifest.py` — regenerates `notes/repo_manifest.json` and `notes/repo_manifest.md` so agents have a current index of the repo tree, authoritative files, and mode-routing map.

## Usage

Refresh the manifest with:

```bash
python3 tools/generate_repo_manifest.py
```

Run this after:

- adding, removing, or renaming files or folders
- changing repo work modes or workflow docs
- changing the top-level structure in a way that affects agent orientation
