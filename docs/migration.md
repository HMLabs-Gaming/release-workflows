# Migrating an existing project

Use this guide when replacing a project's existing CI or release automation with the shared workflows. Migrate one consuming repository at a time. This is a rollout checklist; use the [setup guide](./setup) for a new project or fork.

## Before changing the caller

- Identify which existing steps build, package, publish, and notify.
- Record the actual output filenames, supported loaders/platforms, Minecraft versions, and current release-tag convention.
- Decide which outputs belong on GitHub Releases and which platforms should receive a publish.
- Copy the closest caller example, then replace placeholders with the project's actual build commands and paths.
- Keep any build steps or publishing behavior that the reusable workflow does not provide.

## Rollout

1. Add the new CI caller and run it on a branch. Confirm the build and uploaded Actions artifact.
2. Configure a release caller on `release: published`; set `contents: write` and give it a tested workflow ref.
3. Ensure `workflow-ref` matches the release-workflows tag so the release helper script matches the reusable workflow version.
4. Create a test release from the exact tag intended for shipping. Check out and build behavior, source paths, and both generated asset names for every output.
5. Enable one external publisher at a time. Verify project IDs/slugs, metadata, files, and credentials.
6. Verify the Discord notification, including the release and platform links; provide a valid webhook because the current release workflow has no notification opt-out.
7. Remove the old workflow only after the acceptance criteria pass and the new flow has successfully handled a representative release.

## Acceptance criteria

- CI validates/builds the project and uploads an artifact without external publishing.
- The release build checks out the exact published tag.
- Every configured source file exists and output names are valid and unique before upload.
- Versioned and versionless files are attached to the intended GitHub Release.
- Only supported and actually built variants are configured.
- Fork pull requests do not receive publishing credentials.
- A failed external publisher does not delete successful GitHub Release assets.
- Discord notification runs only after the release succeeds and every configured publisher succeeds or is skipped.

When migrating a multi-platform project, confirm each output is a real variant. A filename label does not create platform compatibility. See [artifact naming](./naming).
