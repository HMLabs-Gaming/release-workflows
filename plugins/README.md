# Plugins

Use `ci.yml` and `release.yml` as caller examples. The central reusable workflows are under `.github/workflows/`.

Configure Java version and build command per project. Artifact JSON should list each output independently and include `loader` such as `spigot`, `paper`, `velocity`, or `universal` only when that label accurately describes the file.

HMTSync is the planned pilot. Keep Hangar, Modrinth, and CurseForge publishing configured per project; SpigotMC remains manual.
