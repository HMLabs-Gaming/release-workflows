# Set up a project or fork

These instructions are for adding the workflows to a consuming Minecraft project, whether it belongs to HMLabs Gaming or is a fork of this workflow repository. Copy the relevant caller examples into the **project repository**; GitHub only exposes files under this repository's `.github/workflows/` as reusable workflows.

## 1. Copy and customize the examples

Choose the closest template and copy its CI and release YAML files into the consuming repository's `.github/workflows/` directory:

| Project         | Templates                                                                                      | Typical build output                               |
| --------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Java mod        | [`mods/`](https://github.com/HMLabs-Gaming/release-workflows/tree/main/mods)                   | One JAR per loader                                 |
| Plugin          | [`plugins/`](https://github.com/HMLabs-Gaming/release-workflows/tree/main/plugins)             | One JAR or distinct platform JARs; optional Hangar |
| Packwiz modpack | [`modpacks/`](https://github.com/HMLabs-Gaming/release-workflows/tree/main/modpacks)           | `.mrpack` and/or `.zip`                            |
| Resource pack   | [`resourcepacks/`](https://github.com/HMLabs-Gaming/release-workflows/tree/main/resourcepacks) | ZIP package                                        |

Before committing, replace the example slug, artifact paths, build/export commands, Java or Go versions, and platform settings. A `loader` is a filename label; it does not build or convert a platform variant.

The checked-in examples reference `@main` to make initial experimentation easy. For normal production use, pin every caller to a tested workflow release tag, for example:

```yaml
uses: HMLabs-Gaming/release-workflows/.github/workflows/ci-java.yml@v1
```

In a release caller, set `workflow-ref: v1` as well, so the workflow and its helper scripts come from the same tested release. When testing a fork, replace `HMLabs-Gaming/release-workflows` with your fork's `OWNER/REPOSITORY`.

## 2. Configure CI

Choose the reusable workflow that matches the project:

- `ci-java.yml`: installs Java, runs `build-command`, then uploads `artifact-paths`.
- `ci-packwiz.yml`: installs Go and Packwiz, runs `validate-command`, then uploads `artifact-paths`.
- `ci-resourcepack.yml`: runs `validate-command`, then uploads `artifact-paths`.

The examples trigger on push, pull request, and manual dispatch. CI needs `contents: read`. It uploads a temporary GitHub Actions artifact; it does not create a release or publish to a platform. For Packwiz, the default installation command tracks Packwiz's `latest` version; set a controlled install command if reproducible tool versions are important to your project.

## 3. Configure a release

The release caller should trigger only when a release is published:

```yaml
on:
  release:
    types: [published]
```

The reusable workflow checks out that exact tag before running the trusted `build-command`. It requires these inputs:

| Input            | Required | Meaning                                                                                            |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `project-slug`   | Yes      | Lowercase kebab-case base name for release assets.                                                 |
| `build-command`  | Yes      | Maintainer-controlled shell commands that build/export the files.                                  |
| `artifacts-json` | Yes      | JSON array of source `path` values and optional `loader` labels.                                   |
| `workflow-ref`   | No       | Ref used to check out helper scripts; defaults to `main`. Align it with the reusable workflow tag. |

The `{version}` placeholder in a source path is replaced with the release tag after removing one leading `v`. The build command must create every configured file. See [naming rules](./naming) for complete examples and validation rules.

Other build inputs:

| Input          | Default | Use                                                              |
| -------------- | ------- | ---------------------------------------------------------------- |
| `java-version` | `25`    | Java version installed for a release build.                      |
| `use-java`     | `true`  | Set `false` for a non-Java build.                                |
| `go-version`   | `1.22`  | Go version installed when requested.                             |
| `use-go`       | `false` | Set `true` when the release build needs Go, for example Packwiz. |

The shell commands are trusted configuration: do not let untrusted pull-request input control them. Release callers need `contents: write` to attach files to a GitHub Release.

## 4. Configure optional publishing

Only add a publisher when that project uses the platform. Provide the relevant project identifier and token, and pass secrets using `secrets: inherit` or explicitly map the required secrets. See [platform publishing](./platform-publishing) and [secrets](./secrets) for details.

Modrinth and CurseForge metadata can be provided with `loaders` and `game-versions`; when omitted, the release workflow attempts best-effort detection from project metadata. Detection is limited and may not describe every multi-platform project, so explicitly set values when detection is incomplete or ambiguous. Hangar platform compatibility is similarly detected from recognized plugin metadata, with an input available to override it.

## 5. Roll out safely

Start with CI on a branch and inspect the uploaded artifact. Then create a test release from the intended tag and check all GitHub Release asset names and files. Enable external publishers one at a time and confirm their uploaded version and files. Keep any old release workflow until the replacement passes these checks. For an existing project, also use the [migration checklist](./migration).
