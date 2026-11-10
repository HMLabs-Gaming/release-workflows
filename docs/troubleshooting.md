# Troubleshooting

## Reusable workflow not found

Check the path under `.github/workflows/`, repository visibility/access, and ref in `uses:`. Only workflows in that directory are reusable endpoints. Caller examples under `mods/`, `plugins/`, `modpacks/`, and `resourcepacks/` must be copied into the consuming repository; they cannot be referenced directly.

For a fork, update the owner and repository in every `uses:` reference, and review repository-specific links and Hangar URLs.

## CI or build errors

- **No artifact matched:** inspect `artifact-paths` after the build or export command. Paths are relative to the checked-out consuming repository; missing matches fail the upload step.
- **Packwiz command missing:** check the install command, Go version, and `PATH`. The template installs the latest Packwiz by default; pin or replace this command if tool reproducibility matters.
- **Release build differs from CI:** the release workflow checks out the published tag, so ensure that tag contains the expected build files and metadata.
- **Command behaves unexpectedly:** `build-command`, `validate-command`, and `packwiz-install-command` are trusted shell configuration. Check quoting and execute them against the same project revision locally.

## Release assets missing or misnamed

- **Release job skipped:** only a `release: published` event runs the release build. Drafts and releases that have only been created do not trigger it.
- **Missing GitHub Release assets:** check caller `contents: write`, published tag, `project-slug`, `artifacts-json`, and that each source path exists after the build.
- **Duplicate output name:** two entries produce the same slug/loader/extension. Give outputs distinct valid loader labels or change the artifact configuration.
- **Invalid slug or loader:** use lowercase kebab-case such as `example-mod` or `fabric`; spaces, underscores, and uppercase letters are invalid.
- **Version mismatch:** one leading lowercase `v` is removed. Allowed version characters are letters, numbers, `.`, `+`, `_`, and `-`. Ensure the tag, build output, and `{version}` source paths agree.
- **Wrong variant published:** a `loader` only affects the asset filename. It does not build, inspect, or convert the artifact. Check the build profiles and actual JAR contents.

## Publisher errors

- **Publisher skipped:** Modrinth and CurseForge require their project IDs; Hangar requires both its project slug and files configuration.
- **Missing credential:** ensure the matching Actions secret exists and the caller passes it with `secrets: inherit` or an explicit mapping.
- **Publisher has no files:** publishers download only versioned outputs. Verify `artifacts-json` created the intended files and that Hangar's paths match files in `platform-assets`.
- **Wrong game versions or loaders:** inspect automatic metadata detection and set explicit `loaders` / `game-versions` when it is incomplete or unsuitable. These explicit values are shared by the configured Modrinth and CurseForge jobs.
- **Hangar compatibility mismatch:** supported metadata detection reads Paper `api-version` from `plugin.yml` and Velocity `supportedVelocityVersions` from `velocity-plugin.json`. Override with `hangar-platform-dependencies` if needed.
- **External publisher failed:** inspect that job's logs. GitHub Release assets are not rolled back; fix the configuration and rerun/release as appropriate.

## Discord notification failed

Confirm `DISCORD_WEBHOOK` is available to the caller and inspect the notification job logs. HTTP 403 responses include provider details; Cloudflare error `1010` means the request was blocked before Discord accepted it. The notification job follows all configured publishers, so a failed configured publisher prevents notification.
