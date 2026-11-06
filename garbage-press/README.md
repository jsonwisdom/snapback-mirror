# Garbage Press Archival Pipeline

Production standard (working specification):

**Source → Verify → Audit → Satire → Cover → Article → Tweet (≤280) → Evidence files → Backup**

## Status
- Independent reconciliation of external figures: UNKNOWN until constituent-level recomputation
- Automatic archival: this pipeline
- AUTHORITY_CREATED: false
- CANON: false

## Usage
Place a production package under `garbage-press/<edition-id>/` containing:
- cover image
- article.md
- tweet.txt
- sources.json or references
- any eJSON evidence

Then dispatch the workflow or push. The packager emits `manifest.ejson` with SHA-256 of every file.

Docker image (local):
```
docker build -t garbage-press-archive .
docker run -v $(pwd)/package:/package garbage-press-archive /package
```
