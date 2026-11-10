# Contributing and maintaining this repository

This is an open source repository and the shared release-workflow library used primarily by HMLabs Gaming's own projects. A change can affect internal releases, external users who track this repository, and people maintaining a fork. Keep all three use cases in mind: internal conventions may be documented as defaults, but avoid baking private project assumptions into reusable behavior.

## Where changes belong

| Change                                         | Look at                                            |
| ---------------------------------------------- | -------------------------------------------------- |
| Reusable workflow behavior or inputs           | `.github/workflows/`                               |
| Project-type caller examples                   | `mods/`, `plugins/`, `modpacks/`, `resourcepacks/` |
| Asset preparation, packaging, or notifications | `scripts/`                                         |
| User-facing guides                             | `docs/` and the top-level `README.md`              |

The template files are copied into consuming repositories; they are not reusable workflow endpoints. Keep their `uses:` references aligned with the reusable workflow names and explain whether an example is a placeholder or an internal convention.

## Change checklist

1. Check the reusable workflow's declared inputs, defaults, permissions, conditions, and jobs before describing behavior.
2. If an input or behavior changes, update relevant examples, documentation, and troubleshooting guidance in the same change.
3. Keep examples safe to publish: use placeholders for project IDs, URLs, and tokens. Never commit credentials, private webhook URLs, or internal-only data.
4. Preserve least privilege. CI should not receive publish tokens, and release build commands should be maintainer-controlled.
5. For workflow or script changes, run the repository validation workflow or its equivalent locally when available. For documentation-only changes, check the links and terminology against current workflow files.
6. In the change description, state the user-visible behavior change and whether callers need to update their configuration.

## Local documentation workflow

The docs use VitePress. From the repository root:

```sh
npm ci
npm run docs:dev
```

Use `npm run docs:build` to generate the static site and `npm run docs:preview` to preview it. Keep navigation in `docs/.vitepress/config.ts` in sync when adding or renaming a guide. The published site URL is configured by the repository's deployment setup.

## Releases and forks

Production consumers should pin reusable workflow calls and `workflow-ref` to a tested release tag. When maintaining a fork, update the organization/repository portion of `uses:` and review every external action, publisher, secret name, and repository-specific link before enabling releases. A fork can adopt only the workflows it needs; platform publishing is optional. Discord notification currently has no opt-out and requires a valid webhook for a fully green release workflow.

The repository's `validate.yml` workflow checks shell syntax, asset naming behavior, and a few required files and documentation markers. It is a baseline check, not a substitute for validating a change against a representative consuming repository and release.
