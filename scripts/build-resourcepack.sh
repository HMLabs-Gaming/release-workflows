#!/usr/bin/env bash
set -Eeuo pipefail

: "${GITHUB_REF_NAME:?GITHUB_REF_NAME is required}"
: "${GITHUB_REPOSITORY:?GITHUB_REPOSITORY is required}"

project_slug="${GITHUB_REPOSITORY##*/}"

python3 - <<'PY'
import json
import os
from pathlib import Path

meta_path = Path("meta.json")
if not meta_path.is_file():
    raise SystemExit("meta.json is required in the resource-pack repository root")

meta = json.loads(meta_path.read_text(encoding="utf-8"))
version = meta.get("version")
if not isinstance(version, str) or not version.strip():
    raise SystemExit("meta.json must contain a non-empty string property 'version'")

version = version.strip()
tag_version = os.environ["GITHUB_REF_NAME"].removeprefix("v")
if version != tag_version:
    raise SystemExit(f"meta.json version ({version}) does not match the release tag ({tag_version})")

print(f"Using resource-pack version {version} from meta.json")
PY

version="$(python3 -c 'import json; print(json.load(open("meta.json", encoding="utf-8"))["version"])')"

zip -qr "${project_slug}-${version}.zip" pack.mcmeta assets pack.png
