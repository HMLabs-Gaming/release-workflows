# Resource-pack templates

Copy [`ci.yml`](ci.yml) and [`release.yml`](release.yml) into the consuming resource-pack repository's `.github/workflows/` directory. Update the validation/package command and project-specific settings.

The release example expects a root `meta.json` with a non-empty string `version` matching the published tag after removing one leading lowercase `v`. It packages `pack.mcmeta`, `assets`, and `pack.png` using the shared helper script; change that command if the project needs additional files. The generated ZIP omits `meta.json` and uses the consuming repository name as its asset slug.

The templates currently call reusable workflows with `@main`. Pin production callers to a tested release tag and align `workflow-ref` in the release caller. See the [setup guide](../docs/setup.md) and [naming rules](../docs/naming.md).
