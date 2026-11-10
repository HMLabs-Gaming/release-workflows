# Secrets and permissions

Keep publishing credentials in the consuming project's repository or organization Actions secrets. Never put secret values in this public repository, workflow inputs, logs, release notes, or artifacts.

## Required permissions by workflow

| Caller  | `GITHUB_TOKEN` permission | Reason                               |
| ------- | ------------------------- | ------------------------------------ |
| CI      | `contents: read`          | Checkout the project source.         |
| Release | `contents: write`         | Attach assets to the GitHub Release. |

Set permissions in the caller workflow using the narrowest access that works. The release workflow declares `contents: write`; CI workflows use read access. Publisher jobs need only read access to the release artifacts they download.

## Optional secrets

| Secret             | Used by              | Required when                                                                                                   |
| ------------------ | -------------------- | --------------------------------------------------------------------------------------------------------------- |
| `MODRINTH_TOKEN`   | Modrinth publisher   | `modrinth-project-id` is configured.                                                                            |
| `CURSEFORGE_TOKEN` | CurseForge publisher | `curseforge-project-id` is configured.                                                                          |
| `HANGAR_API_TOKEN` | Hangar publisher     | Both Hangar project slug and files are configured. Plugins only.                                                |
| `DISCORD_WEBHOOK`  | Release notification | Required for a green release workflow: the current flow always reaches the notification job and has no opt-out. |

The caller can pass secrets with `secrets: inherit` (as the examples do) or explicitly map only those required. The reusable release workflow forwards tokens only to publisher jobs and forwards the Discord webhook to its notification workflow. Do not expose publishing credentials to fork pull requests. Release callers should run on published releases, not pull requests.

## Secret setup checklist

1. Create each token in the platform account with only the project permissions needed to publish.
2. Add the value as an Actions secret in the consuming repository or an appropriate organization secret.
3. Configure the matching publisher ID or slug. A secret by itself does not enable publishing.
4. Test against a suitable non-production project or release before enabling publishing for a live project.
5. Rotate a credential if it appears in a log, commit, issue, or artifact; deleting the visible copy does not invalidate the exposed token.

For which inputs enable each publisher and how files/metadata are selected, see [platform publishing](./platform-publishing).
