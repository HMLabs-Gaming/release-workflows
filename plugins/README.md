# Plugin templates

Copy the caller examples you need into the consuming plugin repository's `.github/workflows/` directory. Replace example project names, commands, profiles, Java versions, and artifact paths before use.

| Template | Intended use |
| --- | --- |
| [`ci.yml`](ci.yml) and [`release.yml`](release.yml) | Single Spigot JAR example. |
| [`multi-jar-ci.yml`](multi-jar-ci.yml) and [`multi-jar-release.yml`](multi-jar-release.yml) | Distinct Spigot, Velocity, and universal build outputs. Remove profiles the project does not support. |
| [`hangar-link-release.yml`](hangar-link-release.yml) | Publish a GitHub Release download link to Hangar without uploading the file to Hangar. |
| [`hangar-link-multi-jar-release.yml`](hangar-link-multi-jar-release.yml) | Publish separate GitHub Release links for platform-specific JARs to Hangar. |

The `loader` value changes the release filename; it does not create a compatible JAR. The default examples use `@main` for experimentation. Pin production callers to a tested release tag and align `workflow-ref` in release callers.

Hangar is supported for plugins only. Its project slug and files configuration enable the job; compatibility can be detected from `src/main/resources/plugin.yml` (`api-version`) and `src/main/resources/velocity-plugin.json` (`supportedVelocityVersions`). See the [publisher guide](../docs/platform-publishing.md), [naming rules](../docs/naming.md), and [setup guide](../docs/setup.md). SpigotMC uploads remain manual.
