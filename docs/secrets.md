# Secrets and permissions

CI does not need third-party publishing tokens. GitHub Release asset upload uses the caller repository's `GITHUB_TOKEN` with `contents: write`.

For optional platform publishing, store tokens in each consuming project's GitHub Actions secrets:
- `MODRINTH_TOKEN`
- `CURSEFORGE_TOKEN`
- `HANGAR_API_TOKEN` (reserved for a separately verified Hangar adapter)

The reusable release workflow supports optional Modrinth and CurseForge jobs. Configure the matching project ID and pass secrets with `secrets: inherit`, or map the required secrets explicitly.

Use the minimum permissions needed. Do not place tokens in repository files, workflow inputs, logs, artifacts, or release notes. Never expose secrets to pull requests from forks.
