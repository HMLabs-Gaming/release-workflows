#!/usr/bin/env bash
set -Eeuo pipefail

: "${PROJECT_SLUG:?PROJECT_SLUG is required}"
: "${RELEASE_VERSION:?RELEASE_VERSION is required}"
: "${ARTIFACTS_JSON:?ARTIFACTS_JSON is required}"

python3 - <<'PY'
import json, os, pathlib, re, shutil, sys

slug = os.environ["PROJECT_SLUG"].strip().lower()
version = os.environ["RELEASE_VERSION"].strip().removeprefix("v")
artifacts = json.loads(os.environ["ARTIFACTS_JSON"])
out = pathlib.Path("release-assets")
out.mkdir(parents=True, exist_ok=True)

def safe(value, label):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise SystemExit(f"Invalid {label}: {value!r}")
    return value

safe(slug, "project slug")
if not re.fullmatch(r"[0-9A-Za-z][0-9A-Za-z.+_-]*", version):
    raise SystemExit(f"Invalid release version: {version!r}")
if not isinstance(artifacts, list) or not artifacts:
    raise SystemExit("ARTIFACTS_JSON must be a non-empty JSON array")

seen = set()
for item in artifacts:
    if not isinstance(item, dict) or not item.get("path"):
        raise SystemExit("Each artifact must have a path")
    src = pathlib.Path(item["path"])
    if not src.is_file():
        raise SystemExit(f"Artifact does not exist: {src}")
    loader = item.get("loader")
    if loader:
        safe(loader.lower(), "loader")
    ext = src.suffix
    if not ext:
        raise SystemExit(f"Artifact has no extension: {src}")
    base = f"{slug}-{loader.lower()}" if loader else slug
    names = [f"{base.rsplit('-', 1)[0]}-{version}-{loader.lower()}{ext}" if loader else f"{slug}-{version}{ext}",
             f"{base}{ext}"]
    # Explicitly avoid confusing a loader suffix with the project slug.
    if loader:
        names = [f"{slug}-{version}-{loader.lower()}{ext}", f"{slug}-{loader.lower()}{ext}"]
    for name in names:
        if name in seen:
            raise SystemExit(f"Duplicate output filename: {name}")
        seen.add(name)
        shutil.copy2(src, out / name)
        print(f"Prepared {out / name}")
PY
