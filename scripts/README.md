# Scripts

- `prepare-release-assets.sh`: copies configured build outputs to versioned and versionless filenames under `release-assets/`. Both variants are intended to be attached to the same GitHub Release.
- Scripts are invoked from a checked-out project repository by reusable workflows. The release workflow checks out the caller project, so the script must be fetched from this workflow repository explicitly before use. See implementation note in the reusable release workflow.
