# HMLabs Gaming Release Workflows

This repository contains reusable GitHub Actions workflows, caller templates, and helper scripts for Minecraft release automation. It is used primarily for HMLabs Gaming's own GitHub and Modrinth projects, while remaining open source for contributors and people who want to fork and adapt it.

The repository serves three related roles:

- **Release workflow library:** central reusable workflows live in `.github/workflows/` and are invoked from other repositories with `uses:`.
- **Template collection:** `mods/`, `plugins/`, `modpacks/`, and `resourcepacks/` contain caller workflow examples to copy into a consuming repository. They are not reusable workflows themselves.
- **Maintained project:** changes here can affect internal projects and external forks, so workflow behavior, examples, scripts, and docs should stay aligned.

Examples contain placeholders and defaults. Replace project-specific names, commands, artifact paths, metadata, and publisher settings before using them. The examples currently point at `@main` for ease of experimentation; pin production callers to a tested release tag.

## Guides

- [Set up a project or fork](./setup)
- [Artifact naming and source paths](./naming)
- [Secrets and permissions](./secrets)
- [Platform publishing](./platform-publishing)
- [Example: HM Basic Play modpack](./examples)
- [Contributing and maintaining this repository](./contributing)
- [Migrating an existing project](./migration)
- [Troubleshooting](./troubleshooting)

## How releases work

Release callers should trigger on `release: published`. The reusable workflow checks out the exact release tag, runs the configured build command, checks every configured source file, then attaches versioned and versionless assets to that GitHub Release. Optional platform jobs publish versioned files to Modrinth, CurseForge, or Hangar. Discord notification is attempted after the release and configured publishers succeed or are skipped. A publisher failure does not roll back assets already attached to GitHub Releases.

CI workflows upload GitHub Actions artifacts only. They do not create a GitHub Release or publish to external platforms.

## Repository links

- [Source repository](https://github.com/HMLabs-Gaming/release-workflows)
- [Mod templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/mods)
- [Plugin templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/plugins)
- [Modpack templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/modpacks)
- [Resource-pack templates](https://github.com/HMLabs-Gaming/release-workflows/tree/main/resourcepacks)
