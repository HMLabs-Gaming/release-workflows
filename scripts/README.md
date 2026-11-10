# Helper scripts

These scripts are called by the reusable workflows after the consuming repository has been checked out. They run in that repository's workspace, not in this repository's root. The release workflow checks out this repository under `.release-workflows` so it can invoke the helpers.

| Script | Purpose and inputs |
| --- | --- |
| `prepare-release-assets.sh` | Validates `PROJECT_SLUG`, `RELEASE_VERSION`, `ARTIFACTS_JSON`, source files, extensions, and duplicate output names. Writes versioned and versionless release files under `release-assets/` and versioned publisher files under `platform-assets/`. |
| `build-resourcepack.sh` | Requires `GITHUB_REF_NAME`, `GITHUB_REPOSITORY`, a root `meta.json`, and the expected pack files. Checks that the metadata version matches the release tag, then creates `<repository>-<version>.zip`. |
| `discord-release.py` | Sends the notification using `DISCORD_WEBHOOK` and performs best-effort platform version lookups without printing tokens. |

When changing a script, check its caller in `.github/workflows/` and update the documentation or caller examples if its inputs or output behavior changes. The repository validation workflow checks shell syntax and release-asset naming behavior. See the [contributor and maintenance guide](../docs/contributing.md).
