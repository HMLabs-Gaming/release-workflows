# Secrets and permissions

CI does not need third-party publishing tokens. GitHub Release asset upload uses the caller repository's `GITHUB_TOKEN` with `contents: write`.

For optional platform publishing, store tokens in each consuming project's GitHub Actions secrets:
- `MODRINTH_TOKEN`
- `CURSEFORGE_TOKEN`
- `HANGAR_API_TOKEN` — only for plugin repositories publishing to Hangar

The reusable release workflow supports optional Modrinth and CurseForge jobs and an optional Hangar job intended only for plugins. Configure the matching project ID/slug and pass secrets with `secrets: inherit`, or map the required secrets explicitly.

Use the minimum permissions needed. Do not place tokens in repository files, workflow inputs, logs, artifacts, or release notes. Never expose secrets to pull requests from forks.
