import json
import os
import urllib.error
import urllib.parse
import urllib.request


def env(name):
    return os.environ.get(name, "").strip()


def get_json(url, headers=None):
    request = urllib.request.Request(url, headers=headers or {}, method="GET")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def modrinth_url(project_id, version):
    if not project_id:
        return ""
    try:
        versions = get_json(f"https://api.modrinth.com/v2/project/{urllib.parse.quote(project_id, safe='')}/version")
        wanted = version.lstrip("v")
        for item in versions:
            if item.get("version_number") == wanted:
                return f"https://modrinth.com/version/{item['id']}"
    except Exception as exc:
        print(f"Warning: Modrinth version lookup failed: {exc}")
    return f"https://modrinth.com/project/{project_id}"


def curseforge_url(project_id, version, token):
    if not project_id:
        return ""
    try:
        headers = {"x-api-key": token, "Accept": "application/json"} if token else {}
        mod = get_json(f"https://api.curseforge.com/v1/mods/{project_id}", headers)["data"]
        slug = mod.get("slug", project_id)
        files = get_json(f"https://api.curseforge.com/v1/mods/{project_id}/files?pageSize=50", headers)["data"]
        wanted = version.lstrip("v")
        for item in files:
            if item.get("displayName") in {version, wanted} or wanted in item.get("fileName", ""):
                return f"https://www.curseforge.com/minecraft/mc-mods/{slug}/files/{item['id']}"
        return f"https://www.curseforge.com/minecraft/mc-mods/{slug}"
    except Exception as exc:
        print(f"Warning: CurseForge version lookup failed: {exc}")
        return f"https://www.curseforge.com/minecraft/mc-mods/{project_id}"


def hangar_url(project_slug, version, token):
    if not project_slug:
        return ""
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        data = get_json(
            f"https://hangar.papermc.io/api/v1/projects/{urllib.parse.quote(project_slug, safe='')}/versions",
            headers,
        )
        versions = data.get("result", data) if isinstance(data, dict) else data
        wanted = version.lstrip("v")
        for item in versions:
            if item.get("name") == wanted:
                return f"https://hangar.papermc.io/{project_slug}/{wanted}"
    except Exception as exc:
        print(f"Warning: Hangar version lookup failed: {exc}")
    return f"https://hangar.papermc.io/{project_slug}"


def main():
    webhook = env("DISCORD_WEBHOOK")
    if not webhook:
        raise SystemExit("DISCORD_WEBHOOK is not configured")

    version = env("VERSION")
    release_url = env("RELEASE_URL")
    links = [f"[GitHub Release]({release_url})"]

    for label, url in (
        ("Modrinth", modrinth_url(env("MODRINTH_PROJECT_ID"), version)),
        ("CurseForge", curseforge_url(env("CURSEFORGE_PROJECT_ID"), version, env("CURSEFORGE_TOKEN"))),
        ("Hangar", hangar_url(env("HANGAR_PROJECT_SLUG"), version, env("HANGAR_API_TOKEN"))),
    ):
        if url:
            links.append(f"[{label}]({url})")

    changelog = env("CHANGELOG")
    if len(changelog) > 3000:
        changelog = changelog[:2997] + "..."

    embed = {
        "title": f"{env('PROJECT_TITLE')} {version} released",
        "url": release_url,
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
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            if not 200 <= response.status < 300:
                raise SystemExit(f"Discord returned HTTP {response.status}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").strip()
        detail = f": {body}" if body else ""
        raise SystemExit(f"Discord returned HTTP {exc.code}{detail}") from exc


if __name__ == "__main__":
    main()
