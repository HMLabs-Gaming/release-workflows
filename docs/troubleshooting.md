# Troubleshooting

- **Reusable workflow not found:** check the path under `.github/workflows/`, repository visibility/access, and the ref (tag or branch).
- **No artifact matched:** verify `artifact-paths` and run the build command locally or in CI; missing configured files should fail the job.
- **Missing release assets:** check the release tag, `artifacts-json` paths, project slug, and permissions for `contents: write`.
- **Duplicate output name:** two entries produce the same slug/loader/extension. Give the outputs distinct valid loader names or adjust the artifact configuration.
- **Release version mismatch:** tags may start with `v`; the naming script strips only the leading `v`. Keep project metadata and release tag versions aligned.
- **External platform upload failed:** inspect that platform's job logs and retry only that publisher job where supported. Do not assume the GitHub Release upload was rolled back.
