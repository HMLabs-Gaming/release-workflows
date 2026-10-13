# Platform publishing

The reusable release workflow supports optional, independent publisher jobs. All publishers consume the versioned build files; both versioned and versionless files are attached to the same GitHub Release.

## Modrinth and CurseForge

These publishers are optional for mods, plugins, modpacks, and resource packs. They run only when the matching project ID is configured.

Inputs:
- `modrinth-project-id`
- `curseforge-project-id`
- `version-type` (`release`, `beta`, or `alpha`)
- `loaders` (newline-separated platform loader IDs)
- `game-versions` (newline-separated Minecraft versions)

Pass project repository secrets using `secrets: inherit`, or explicitly map `MODRINTH_TOKEN` and `CURSEFORGE_TOKEN`.

## Hangar — plugins only

Hangar publishing is supported by a separate job in the reusable release workflow and should only be configured from `plugins/release.yml`. Do not enable it for mods, modpacks, or resource packs.

Configure:
- `hangar-project-slug`: the project's actual Hangar slug; leave empty to disable publishing.
- `hangar-channel`: normally `Release`, or `Beta` / `Alpha` if configured on the Hangar project.
- `hangar-files`: JSON array mapping each versioned file to its Hangar platforms.
- `hangar-platform-dependencies`: JSON object with supported versions for each platform, for example `{"PAPER":[">=1.21"],"VELOCITY":[">=3.0.0"]}`.
- Repository Actions secret `HANGAR_API_TOKEN`, passed to the action as `api_token`.

Example for a plugin that creates separate Paper and Velocity JARs:
```json
[
  {"path":"platform-assets/hmt-sync-*-spigot.jar","platforms":["PAPER"]},
  {"path":"platform-assets/hmt-sync-*-velocity.jar","platforms":["VELOCITY"]}
]
```

The paths are relative to the downloaded `platform-assets` directory and should match only versioned outputs. Configure the real Hangar slug and supported platform versions before enabling the job. If either the Hangar slug or files configuration is empty, the Hangar job is skipped.

## SpigotMC

SpigotMC remains a manual upload; no unsupported API automation is assumed. Keep publisher jobs independent so a platform failure does not remove successfully attached GitHub Release assets.
