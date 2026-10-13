# Secrets and permissions

The initial generic CI and GitHub Release asset workflows require no third-party publishing tokens.

When platform publishing adapters are added/configured, store tokens in each consuming project repository's GitHub Actions secrets:
- `MODRINTH_TOKEN`
- `CURSEFORGE_TOKEN`
- `HANGAR_API_TOKEN`

Use the minimum permissions needed. Do not place tokens in repository files, workflow inputs, logs, artifacts, or release notes. Do not expose secrets to pull requests from forks. A GitHub Release upload uses the caller repository's `GITHUB_TOKEN` with `contents: write` scoped to the release job.
