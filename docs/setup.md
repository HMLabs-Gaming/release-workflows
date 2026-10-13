# Setup guide

## Caller workflow files

Reusable workflows must live under `.github/workflows/` in this repository. Each project repository also keeps its own small caller files under `.github/workflows/`. The `mods/`, `plugins/`, `modpacks/`, and `resourcepacks/` folders here contain organized examples and instructions.

## CI

Use `HMLabs-Gaming/release-workflows/.github/workflows/ci-java.yml@main` for Java/Maven or Gradle projects, `ci-packwiz.yml@main` for Packwiz modpacks, and `ci-resourcepack.yml@main` for resource packs. After validating a release of this workflow repository, change `@main` to a stable tag such as `@v1`.

## Release

A project release caller should run on `release: types: [published]` and call `release-artifacts.yml`. Configure:
- `project-slug`
- `build-command`
- `artifacts-json`: JSON array of built source paths and optional loader names
- Java/Go setup flags as needed

Example artifacts JSON:
`[{"path":"target/hmt-sync-1.0.2-spigot.jar","loader":"spigot"},{"path":"target/hmt-sync-1.0.2-velocity.jar","loader":"velocity"},{"path":"target/hmt-sync-1.0.2-universal.jar","loader":"universal"}]`

Optional platform publishing can be enabled with `modrinth-project-id` and/or `curseforge-project-id`, plus `version-type`, `loaders`, and `game-versions`. Add `secrets: inherit` to the caller job and configure `MODRINTH_TOKEN` / `CURSEFORGE_TOKEN` in the consuming repository. Each platform publisher is a separate job. Hangar is not yet wired into the reusable workflow.\n\nWhen pinning a caller to `@v1`, also set `workflow-ref: v1` so the naming script comes from the same tagged version.\n\nBuild commands are executable shell input. Only trusted maintainers should edit caller workflows or their build commands.

## First-time repository configuration

- Allow GitHub Actions to access reusable workflows from this public repository.
- Configure minimal permissions on each project.
- Add platform tokens only when the corresponding publisher job is configured.
- Never pass publishing secrets to fork pull requests.
- Keep existing project workflows until the migrated workflows pass a test release.
