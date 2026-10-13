# Migration plan

Migrate incrementally. Do not delete or disable an existing project workflow until its central replacement has been tested.

1. Validate the reusable workflow syntax and artifact-naming script.
2. Pilot HMTSync CI and confirm downloadable GitHub Actions artifacts.
3. Pilot HMTSync release asset generation; verify all versioned and versionless JARs appear on the same GitHub Release.
4. Migrate HMTAPI.
5. Migrate Packwiz modpacks and validate Modrinth/CurseForge exports.
6. Migrate resource packs.
7. Migrate mods and loader-specific artifacts.
8. Configure and verify platform publishing adapters independently.
9. Keep SpigotMC publishing manual unless a supported API integration is confirmed.

Acceptance criteria:
- CI builds and exposes artifacts without publishing externally.
- Releases build from the exact published tag.
- Every configured output has both filenames attached to that same GitHub Release.
- Duplicate or missing outputs fail before upload.
- Fork PRs cannot access publishing tokens.
- Failure in an external platform upload does not invalidate successful GitHub assets.
