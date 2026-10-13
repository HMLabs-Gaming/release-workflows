# Plugins

Use `ci.yml` and `release.yml` as caller examples. The central reusable workflows are under `.github/workflows/`.

Configure Java version and build command per project. Artifact JSON should list each output independently and include `loader` such as `spigot`, `paper`, `velocity`, or `universal` only when that label accurately describes the file.

Hangar is supported for plugins only. Set the actual Hangar project slug, channel, versioned file-to-platform mappings, platform version metadata, and the `HANGAR_API_TOKEN` Actions secret in the consuming plugin repository. Leave Hangar settings empty to disable the publisher. SpigotMC remains manual.
