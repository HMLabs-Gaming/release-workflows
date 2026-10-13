# HMLabs Gaming Release Workflows

Central templates for CI and release automation for Minecraft mods, plugins, modpacks, and resource packs.

## Important GitHub Actions constraint

GitHub only loads reusable workflow files from `.github/workflows/`. The `mods/`, `plugins/`, `modpacks/`, and `resourcepacks/` folders in this repository therefore contain **project-side caller examples and documentation**, not directly callable reusable workflows. The actual reusable workflows live under `.github/workflows/`. Project repositories use small caller files under their own `.github/workflows/` directory.

## Project types

- `mods/`: mod CI and release caller examples
- `plugins/`: plugin CI and release caller examples
- `modpacks/`: Packwiz CI and release caller examples
- `resourcepacks/`: ZIP resource-pack CI and release caller examples

## Artifact naming

Every release artifact is attached to the GitHub Release in both versioned and unversioned form.

With a loader:
- `<slug>-<version>-<loader>.<ext>`
- `<slug>-<loader>.<ext>`

Without a loader:
- `<slug>-<version>.<ext>`
- `<slug>.<ext>`

Examples:
- `hmt-sync-1.0.2-spigot.jar` and `hmt-sync-spigot.jar`
- `hm-basic-play-3.2.0.mrpack` and `hm-basic-play.mrpack`
- `js-green-ores-1.5.0.zip` and `js-green-ores.zip`

Loader names are only included when the artifact actually targets a specific loader/platform. Use `universal` only when one artifact works for all configured targets. Modpack formats are distinguished by extension, not loader.

The versionless assets are attached to each release too. For a stable latest-release URL, use:
`https://github.com/OWNER/REPOSITORY/releases/latest/download/ASSET_NAME`

## Safety and release rules

- CI runs builds/tests and uploads downloadable GitHub Actions artifacts; it does not publish to external platforms.
- Release workflows build from the published release tag and attach all versioned and versionless assets to that GitHub Release.
- This initial implementation handles CI artifacts and GitHub Release assets. Platform-specific Modrinth, CurseForge, and Hangar publishing adapters are not yet wired into the reusable release workflow; see [platform publishing status](docs/platform-publishing.md).
- Fork pull requests must never receive publishing tokens.
- Keep permissions minimal and pin reusable workflow references to a released tag such as `@v1` once this repository has a tested release.
- Migrate project repositories incrementally. Keep existing workflows until the central version is verified for that project.

## Getting started

See [setup guide](docs/setup.md), [naming rules](docs/naming.md), [secrets](docs/secrets.md), [platform publishing status](docs/platform-publishing.md), [migration plan](docs/migration.md), and [troubleshooting](docs/troubleshooting.md).
