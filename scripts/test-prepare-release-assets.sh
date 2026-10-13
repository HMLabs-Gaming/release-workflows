#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cd "$TMP"
mkdir -p target
printf 'plugin jar\n' > target/plugin.jar
printf 'resource zip\n' > target/pack.zip
PROJECT_SLUG=hmt-sync RELEASE_VERSION=v1.2.3 ARTIFACTS_JSON='[{"path":"target/plugin.jar","loader":"universal"}]' bash "$ROOT/scripts/prepare-release-assets.sh"
test -f release-assets/hmt-sync-1.2.3-universal.jar
test -f release-assets/hmt-sync-universal.jar
PROJECT_SLUG=example-pack RELEASE_VERSION=2.0.0 ARTIFACTS_JSON='[{"path":"target/pack.zip"}]' bash "$ROOT/scripts/prepare-release-assets.sh"
test -f release-assets/example-pack-2.0.0.zip
test -f release-assets/example-pack.zip
