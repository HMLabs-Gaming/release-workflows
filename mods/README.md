# Mod templates

These are caller workflow templates for a consuming mod repository. Copy [`ci.yml`](ci.yml) and [`release.yml`](release.yml) to that repository's `.github/workflows/` directory, then replace example commands, slug, Java version, and artifact path with the project's actual configuration.

The CI example builds on pushes, pull requests, and manual dispatch, then uploads matching JAR files as a GitHub Actions artifact. The release example runs only for a published GitHub Release and attaches configured outputs to that release. List each real loader output separately in `artifacts-json`; configure Modrinth or CurseForge only when the project is published there.

The templates currently call reusable workflows with `@main`. Pin both calls to a tested release tag for production use, and keep `workflow-ref` aligned in the release caller. See the [setup guide](../docs/setup.md), [naming rules](../docs/naming.md), and [publisher guide](../docs/platform-publishing.md).
