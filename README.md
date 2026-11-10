# HMLabs Gaming Release Workflows

Reusable GitHub Actions workflows, example callers, and scripts for building and publishing Minecraft mods, plugins, modpacks, and resource packs.

This repository is the release-workflow library and template repository used primarily by HMLabs Gaming's own GitHub and Modrinth projects. It is public and open source so contributors can improve it and other people can fork it for their own projects. The examples are starting points: replace project names, commands, paths, metadata, and publishing settings before using them.

## Choose a starting point

- New project or a fork: read the [setup guide](https://release-workflows.gaming.hmlabs.eu/setup.html), then copy the matching caller example from [`mods/`](mods/), [`plugins/`](plugins/), [`modpacks/`](modpacks/), or [`resourcepacks/`](resourcepacks/).
- Maintaining this workflow library: read the [repository overview](https://release-workflows.gaming.hmlabs.eu/), [contributor and maintenance guide](https://release-workflows.gaming.hmlabs.eu/contributing.html), and [migration guide](https://release-workflows.gaming.hmlabs.eu/migration.html).
- Understanding output names: see [artifact naming](https://release-workflows.gaming.hmlabs.eu/naming.html).
- Setting up publishing credentials: see [secrets and permissions](https://release-workflows.gaming.hmlabs.eu/secrets.html) and [platform publishing](https://release-workflows.gaming.hmlabs.eu/platform-publishing.html).
- Seeing a real Modrinth and CurseForge release flow: read the [HM Basic Play example](https://release-workflows.gaming.hmlabs.eu/examples.html).

## Repository layout

| Path                                               | Purpose                                                                                                                       |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `.github/workflows/`                               | Reusable workflows that callers reference with `uses:`; `validate.yml` checks this repository.                                |
| `mods/`, `plugins/`, `modpacks/`, `resourcepacks/` | Caller workflow templates to copy into a consuming repository. GitHub cannot call these files directly as reusable workflows. |
| `scripts/`                                         | Helper scripts checked out and run by reusable workflows, plus their documentation.                                           |
| `docs/`                                            | VitePress documentation published at the project documentation site.                                                          |

## Release behavior

- CI caller examples run on pushes, pull requests, and manual dispatch, then upload GitHub Actions artifacts. CI does not publish releases or platform versions.
- The release workflow runs only for a published GitHub Release, builds from that exact release tag, validates the configured source files, and attaches versioned assets plus stable versionless aliases to the GitHub Release.
- Modrinth, CurseForge, and Hangar publishing are optional jobs. Hangar support is for plugins; SpigotMC uploads are manual. External publishers use versioned files, while both names remain on GitHub Releases.
- Discord notification runs after the release build and all configured publishers succeed or are skipped. The current workflow has no notification opt-out: a missing or invalid `DISCORD_WEBHOOK` makes that job fail after GitHub assets may already be uploaded.
- A failure at an external publisher does not remove GitHub Release assets that were already uploaded.

Use a tested release-workflows tag such as `@v1` for production callers and set `workflow-ref: v1` to the same tag in release callers. The checked-in templates use `@main` so they work against the current development branch; pin them before adopting them for production. The Discord notification workflow currently fetches its helper script from `main`, so that part is not pinned by the release caller; see [platform publishing](https://release-workflows.gaming.hmlabs.eu/platform-publishing.html).

## Contributing

Changes to reusable workflows can affect every caller, including internal projects. Keep examples and docs in sync with workflow inputs and behavior, and use the [contributor and maintenance guide](https://release-workflows.gaming.hmlabs.eu/contributing.html) for the change checklist. Never add real project credentials or private webhook URLs to this public repository.

## License

See [LICENSE](LICENSE).
