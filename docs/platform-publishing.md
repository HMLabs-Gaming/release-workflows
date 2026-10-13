# Platform publishing status

The first implementation establishes reusable CI and release-asset generation. The generic release workflow attaches both filename variants to GitHub Releases.

External publishing adapters are a separate follow-up because each platform has different required metadata and artifact rules:
- **Modrinth:** project ID, token, version type, supported game versions/loaders, and platform-specific file selection.
- **CurseForge:** project ID, token, game versions/loaders, and release type.
- **Hangar:** project ID, API token, platform-specific version metadata and supported upload action.
- **SpigotMC:** remains manual; no supported API automation is assumed.

Do not add a publisher to a project until its project IDs and metadata are configured and a test release can be verified. Publisher jobs should be independent so a platform failure does not undo successfully attached GitHub Release assets. Keep all tokens in consuming-repository Actions secrets.
