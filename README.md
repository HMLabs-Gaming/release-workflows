# HMLabs Gaming Release Workflows

Central reusable GitHub Actions workflows and caller examples for Minecraft mods, plugins, modpacks, and resource packs.

## Repository layout and GitHub Actions constraint

GitHub only loads reusable workflow files from `.github/workflows/`. The `mods/`, `plugins/`, `modpacks/`, and `resourcepacks/` folders therefore contain organized caller examples and documentation, not directly callable reusable workflows. Consuming projects copy these examples into their own `.github/workflows/` directory and call the central workflows.

- `.github/workflows/ci-java.yml`: Java/Maven or Gradle CI
- `.github/workflows/ci-packwiz.yml`: Packwiz modpack CI
- `.github/workflows/ci-resourcepack.yml`: resource-pack CI
- `.github/workflows/release-artifacts.yml`: release assets and optional platform publishing
- `.github/workflows/validate.yml`: repository smoke tests

## Artifact naming

Every release output is attached to the same GitHub Release in both versioned and versionless form.

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

Use `universal` only when the same binary supports all configured targets. Modpack formats are distinguished by extension, not loader. The versionless assets are attached to every release too; stable latest links follow:
`https://github.com/OWNER/REPOSITORY/releases/latest/download/ASSET_NAME`

## CI and release behavior

- CI builds/tests and uploads downloadable GitHub Actions artifacts; it does not publish externally.
- Release workflows build from the published tag, generate both filename variants, and attach every variant to that GitHub Release.
- Optional independent Modrinth and CurseForge jobs publish versioned assets when project IDs and tokens are configured.
- Hangar needs a separately verified adapter; SpigotMC remains manual.
- Fork pull requests must never receive publishing tokens.
- Pin reusable workflow references to a tested release tag (for example `@v1`) once a tag is published, and set `workflow-ref` to the same tag.
- Migrate projects incrementally and retain old workflows until each migration is verified.

## Documentation

See [setup](docs/setup.md), [naming](docs/naming.md), [secrets](docs/secrets.md), [platform publishing](docs/platform-publishing.md), [migration](docs/migration.md), and [troubleshooting](docs/troubleshooting.md).
