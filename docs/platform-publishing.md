# Platform publishing

The reusable release workflow attaches assets to GitHub Releases first, then starts optional platform publisher jobs. Publisher jobs consume the versioned files; GitHub Releases retain both the versioned asset and its versionless alias. A failed platform job does not remove files already attached to the GitHub Release.

Only configure platforms that the project actually uses. Keep IDs, slugs, metadata, and credentials specific to the consuming repository. See [secrets and permissions](./secrets) for credential setup.

## Modrinth and CurseForge

Both publishers support mods, plugins, modpacks, and resource packs. A publisher runs when its project ID is non-empty; its token must also be available to the reusable workflow.

| Input                   | Purpose                                               |
| ----------------------- | ----------------------------------------------------- |
| `modrinth-project-id`   | Enables Modrinth publishing.                          |
| `curseforge-project-id` | Enables CurseForge publishing.                        |
| `version-type`          | `release`, `beta`, or `alpha`; defaults to `release`. |
| `loaders`               | Optional newline-separated platform loader IDs.       |
| `game-versions`         | Optional newline-separated Minecraft versions.        |

When loader or game-version inputs are empty, the release workflow attempts limited metadata detection:

- Resource pack: root `meta.json` with `minecraft.from` and/or `minecraft.to`.
- Fabric project: `gradle.properties` with `minecraft_version`, or `src/main/resources/fabric.mod.json` with a Minecraft dependency range.
- Packwiz: `platforms/modrinth/pack.toml`, `platforms/curseforge/pack.toml`, or root `pack.toml`.
- Paper plugin: `src/main/resources/plugin.yml` with `api-version`.

Detection is best effort, not a complete project model. In particular, one project can produce several files for different loaders or platforms. Set explicit metadata if detection is absent, incomplete, or unsuitable for the platform/project. The provided loader list is applied to both configured publishers; if their platform classifications differ, check the publisher's accepted values and adjust the workflow or metadata deliberately.

## Hangar (plugins only)

Hangar is supported for plugin projects. The job runs only when both `hangar-project-slug` and `hangar-files` are non-empty.

| Input                          | Purpose                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `hangar-project-slug`          | Actual Hangar project slug.                                                  |
| `hangar-channel`               | Hangar channel such as `Release`, `Beta`, or `Alpha`; defaults to `Release`. |
| `hangar-files`                 | JSON array describing uploaded files or external download links.             |
| `hangar-platform-dependencies` | Optional JSON object overriding detected compatibility versions.             |

For uploaded files, paths are relative to the downloaded `platform-assets` directory, which contains versioned artifacts only:

```yaml
hangar-files: '[{"path":"platform-assets/example-plugin-*-paper.jar","platforms":["PAPER"]}]'
```

For external GitHub Release links, use `url: true` and `externalUrl`; `{tag}` expands to the full release tag and `{version}` to the tag without a leading `v`:

```yaml
hangar-files: '[{"platforms":["PAPER"],"url":true,"externalUrl":"https://github.com/OWNER/REPOSITORY/releases/download/{tag}/example-plugin-{version}.jar"}]'
```

Replace `OWNER`, `REPOSITORY`, slug, file names, platforms, and compatibility values with those for the consuming project. The job can detect Paper compatibility from `src/main/resources/plugin.yml` (`api-version`) and Velocity compatibility from `src/main/resources/velocity-plugin.json` (`supportedVelocityVersions`). If no supported metadata is found, set `hangar-platform-dependencies` explicitly. The [plugin templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/plugins) include uploaded-file and external-link examples.

## Discord notification

The notification job runs after the GitHub Release build succeeds and each configured Modrinth, CurseForge, and Hangar job succeeds or is skipped. It sends the release URL and changelog, plus best-effort links to configured platforms. There is no project input to disable it: every successful release flow reaches this job. If `DISCORD_WEBHOOK` is absent or invalid, the notification fails even though GitHub Release assets may already have been uploaded. The nested notification workflow currently references this repository's `main` branch for its script, so pinning the release workflow alone does not pin that notification implementation.

## SpigotMC

SpigotMC publishing remains a manual upload. The reusable workflow does not automate it. Keep platform failures separate from GitHub Release asset creation and verify platform uploads against the files attached to the release.
