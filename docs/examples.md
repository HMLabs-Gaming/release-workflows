# Example: HM Basic Play modpack

[HM Basic Play](https://github.com/HMLabs-Gaming/hm-basic-play) is a real Packwiz modpack that uses this repository's reusable workflows. Its CI exports Modrinth and CurseForge formats, and its published-release workflow builds and publishes the pack to GitHub Releases, Modrinth, and CurseForge.

This example reflects the caller configuration on the repository's current default branch. Workflow runs, release history, project metadata, and service interfaces can change; use the linked source files as the current reference.

## Project and workflow links

- [HM Basic Play source repository](https://github.com/HMLabs-Gaming/hm-basic-play)
- [All GitHub Actions runs](https://github.com/HMLabs-Gaming/hm-basic-play/actions)
- [CI run history](https://github.com/HMLabs-Gaming/hm-basic-play/actions/workflows/ci.yml)
- [Release run history](https://github.com/HMLabs-Gaming/hm-basic-play/actions/workflows/release.yml)
- [CI caller workflow](https://github.com/HMLabs-Gaming/hm-basic-play/blob/main/.github/workflows/ci.yml)
- [Release caller workflow](https://github.com/HMLabs-Gaming/hm-basic-play/blob/main/.github/workflows/release.yml)
- [Modrinth project](https://modrinth.com/modpack/hm-basic-play) · [Modrinth versions](https://modrinth.com/modpack/hm-basic-play/versions)
- [CurseForge project](https://www.curseforge.com/minecraft/modpacks/hm-basic-play) · [CurseForge files](https://www.curseforge.com/minecraft/modpacks/hm-basic-play/files/all?page=1&pageSize=20&showAlphaFiles=hide)

## What happens in CI

The [CI caller](https://github.com/HMLabs-Gaming/hm-basic-play/blob/main/.github/workflows/ci.yml) invokes `ci-packwiz.yml`. On pushes, pull requests, and manual dispatch it:

1. Installs Go and Packwiz.
2. Runs the repository's platform-parity check so the Modrinth and CurseForge pack definitions stay aligned.
3. Exports an `.mrpack` from `platforms/modrinth/` and a `.zip` from `platforms/curseforge/`.
4. Uploads both exports as a GitHub Actions artifact for inspection.

CI does not publish to Modrinth or CurseForge. It validates the content and makes the generated files available on the Actions run.

## What happens on a published release

The [release caller](https://github.com/HMLabs-Gaming/hm-basic-play/blob/main/.github/workflows/release.yml) runs only for a published GitHub Release. It calls `release-artifacts.yml` with the `hm-basic-play` slug and the Modrinth and CurseForge project IDs. Its build command:

1. Updates the version in both Packwiz manifests to match the GitHub release tag.
2. Installs Packwiz and exports both platform formats from the tagged source.
3. Passes the resulting `.mrpack` and `.zip` paths to `artifacts-json`.

The reusable workflow attaches versioned and versionless copies of the configured files to that GitHub Release, then runs the enabled Modrinth and CurseForge publisher jobs. Each publisher needs its matching Actions secret in the consuming repository. The workflow can also detect the Minecraft version and Fabric loader from the Packwiz manifest when explicit publisher metadata is omitted.

The external project IDs are configuration, not credentials. Publishing tokens stay in GitHub Actions secrets and are passed to the reusable workflow with `secrets: inherit`.

## Adapt the pattern

For your own Packwiz project, copy the [modpack templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/modpacks) into its `.github/workflows/` directory. Then adapt:

- platform-specific Packwiz manifest paths and export commands;
- the parity check, or an equivalent check appropriate to your project;
- project slug and output paths in `artifacts-json`;
- Modrinth and CurseForge project IDs and Actions secrets;
- `@main` refs to a tested release-workflows tag for production use.

See the [modpack setup guide](./setup), [modpack templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/modpacks), and [platform publishing guide](./platform-publishing) for the reusable configuration details.
