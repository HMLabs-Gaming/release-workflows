# Platform publishing

The reusable release workflow supports optional, independent Modrinth and CurseForge publisher jobs. These jobs only run when the corresponding project ID is configured.

Configure the following reusable-workflow inputs in a project caller:
- `modrinth-project-id`
- `curseforge-project-id`
- `version-type` (`release`, `beta`, or `alpha`)
- `loaders` (newline-separated platform loader IDs)
- `game-versions` (newline-separated Minecraft versions)

Pass project repository secrets using `secrets: inherit`, or explicitly map `MODRINTH_TOKEN` and `CURSEFORGE_TOKEN`. A configured project ID without its matching token should fail visibly. The publisher jobs upload only the versioned build files; both versioned and versionless files are attached to the GitHub Release.

Hangar still needs a separately verified adapter and project metadata. SpigotMC remains manual; no unsupported API automation is assumed. Keep publisher jobs independent so a platform failure does not remove successfully attached GitHub Release assets.
