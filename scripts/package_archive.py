#!/usr/bin/env python3
"""
Garbage Press Archival Packager
Computes SHA-256 for production files and emits an eJSON evidence manifest.
Usage: python package_archive.py /path/to/package
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: package_archive.py <package_dir>", file=sys.stderr)
        sys.exit(1)

    package_dir = Path(sys.argv[1])
    if not package_dir.is_dir():
        print(f"Not a directory: {package_dir}", file=sys.stderr)
        sys.exit(1)

    files = []
    for p in sorted(package_dir.rglob("*")):
        if p.is_file() and p.name != "manifest.ejson":
            rel = p.relative_to(package_dir)
            files.append({
                "path": str(rel),
                "sha256": sha256_file(p),
                "size": p.stat().st_size
            })

    manifest = {
        "protocol": "GARBAGE_PRESS_ARCHIVE_V0_1",
        "standard": "Source → Verify → Audit → Satire → Cover → Article → Tweet → Evidence files → Backup",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "package_id": package_dir.name,
        "files": files,
        "independent_reconciliation": "UNKNOWN",
        "authority_created": False,
        "canon": False
    }

    out = package_dir / "manifest.ejson"
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Wrote {out}")
    print(json.dumps({"file_count": len(files), "manifest": str(out)}, indent=2))

if __name__ == "__main__":
    main()
