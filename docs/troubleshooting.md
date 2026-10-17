# Troubleshooting

- **Reusable workflow not found:** check the path under `.github/workflows/`, repository visibility/access, and the ref (tag or branch).
- **No artifact matched:** verify `artifact-paths` and run the build command locally or in CI; missing configured files should fail the job.
- **Missing release assets:** check the release tag, `artifacts-json` paths, project slug, and permissions for `contents: write`.
- **Duplicate output name:** two entries produce the same slug/loader/extension. Give the outputs distinct valid loader names or adjust the artifact configuration.
- **Release version mismatch:** tags may start with `v`; the naming script strips only the leading `v`. Keep project metadata and release tag versions aligned.
- **External platform upload failed:** inspect that platform's job logs and retry only that publisher job where supported. Do not assume the GitHub Release upload was rolled back.
- **Discord notification failed:** confirm that the consuming release caller uses `secrets: inherit` and that an Organization or repository Actions secret named `DISCORD_WEBHOOK` is available to that repository. The central workflow forwards it to the nested notification workflow. If the notification step reaches Discord but returns HTTP 403, inspect the response detail; Cloudflare error code `1010` indicates the request was blocked before Discord accepted the webhook request.
