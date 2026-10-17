import json
import os
import urllib.request


def env(name):
    return os.environ.get(name, "").strip()


def main():
    webhook = env("DISCORD_RELEASE_WEBHOOK")
    if not webhook:
        raise SystemExit("DISCORD_RELEASE_WEBHOOK is not configured")

    fields = []
    links = []
    for label, key in (("GitHub Release", "RELEASE_URL"), ("Modrinth", "MODRINTH_URL"), ("CurseForge", "CURSEFORGE_URL"), ("Hangar", "HANGAR_URL")):
        url = env(key)
        if url:
            links.append(f"[{label}]({url})")

    changelog = env("CHANGELOG")
    if len(changelog) > 3000:
        changelog = changelog[:2997] + "..."

    embed = {
        "title": f"{env('PROJECT_TITLE')} {env('VERSION')} released",
        "url": env("RELEASE_URL"),
        "description": changelog or "A new version has been released.",
        "fields": [{"name": "Downloads", "value": " • ".join(links), "inline": False}],
    }

    payload = {"embeds": [embed]}
    request = urllib.request.Request(
        webhook,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status < 200 or response.status >= 300:
            raise SystemExit(f"Discord returned HTTP {response.status}")


if __name__ == "__main__":
    main()
