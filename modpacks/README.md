# Modpack templates

Copy [`ci.yml`](ci.yml) and [`release.yml`](release.yml) into the consuming Packwiz repository's `.github/workflows/` directory. Update the Go and Packwiz setup, validation/export commands, slug, and output paths for the project's layout.

The CI example exports Modrinth and CurseForge formats and uploads matching files as a GitHub Actions artifact. The release example runs the configured build/export commands from the published tag and attaches each configured output to its GitHub Release. Configure `.mrpack` and `.zip` paths only for formats the project actually exports; a loader label is usually unnecessary for these formats.

The templates currently call reusable workflows with `@main`. Pin production callers to a tested release tag and align `workflow-ref` in the release caller. The example installs Packwiz from `@latest`, so choose an explicit version or install command if reproducible tooling is required. See the [setup guide](../docs/setup.md) and [naming rules](../docs/naming.md).

For a working end-to-end project that exports both Modrinth and CurseForge formats and publishes releases to both platforms, see the [HM Basic Play example](../docs/examples.md).
