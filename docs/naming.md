# Artifact naming rules

Each final build output is published twice to the **same GitHub Release**: a versioned asset and a versionless alias asset.

| Target | Versioned | Versionless |
|---|---|---|
| Loader-specific | `<slug>-<version>-<loader>.<ext>` | `<slug>-<loader>.<ext>` |
| No loader | `<slug>-<version>.<ext>` | `<slug>.<ext>` |

Examples:
- `hmt-sync-1.0.2-spigot.jar` and `hmt-sync-spigot.jar`
- `hmt-sync-1.0.2-universal.jar` and `hmt-sync-universal.jar`
- `example-mod-2.4.0-fabric.jar` and `example-mod-fabric.jar`
- `hm-basic-play-3.2.0.mrpack` and `hm-basic-play.mrpack`
- `hm-basic-play-3.2.0.zip` and `hm-basic-play.zip`
- `js-green-ores-1.5.0.zip` and `js-green-ores.zip`

## Source artifact paths

In `artifacts-json`, use the `{version}` placeholder whenever the built file itself contains the release version, for example:

```yaml
artifacts-json: '[{"path":"platforms/modrinth/example-modpack-{version}.mrpack"},{"path":"platforms/curseforge/example-modpack-{version}.zip"}]'
```

The workflow replaces `{version}` with the release tag without a leading `v` before checking the source path. The source path must match the actual filename produced by the build/export command. For outputs that do not include a version in their source filename, use the literal path and let the workflow generate versioned release asset names.

Rules:
- Use lowercase kebab-case for slugs and loader names.
- Remove a leading `v` from a release tag when constructing filenames.
- Omit loader for resource packs and modpacks unless a genuine loader-specific output is configured.
- Use `universal` only when the same binary supports all declared targets.
- Keep extensions from the actual built artifact.
- Fail the release if a configured source file is missing or output names collide.
- The versionless file is an additional asset, not a replacement for the versioned file.

Stable URL pattern:
`https://github.com/OWNER/REPOSITORY/releases/latest/download/ASSET_NAME`
