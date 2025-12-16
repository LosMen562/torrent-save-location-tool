import requests
from urllib.parse import urljoin

# ==============================
# CONFIG
# ==============================
QB_HOST = "http://localhost:8080"
QB_USER = "admin"
QB_PASS = "Carter063020!"

# ==============================
# AUTH SESSION
# ==============================
session = requests.Session()

login_url = urljoin(QB_HOST, "/api/v2/auth/login")
resp = session.post(login_url, data={
    "username": QB_USER,
    "password": QB_PASS
})

if resp.text != "Ok.":
    raise RuntimeError("Failed to authenticate with qBittorrent")

# ==============================
# FETCH TORRENTS
# ==============================
torrents_url = urljoin(QB_HOST, "/api/v2/torrents/info")
torrents = session.get(torrents_url).json()

# ==============================
# OUTPUT
# ==============================
output_file = "torrent_save_locations.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("=" * 100 + "\n")
    f.write(f"{'NAME':40} {'STATE':12} {'CATEGORY':10} SAVE PATH\n")
    f.write("=" * 100 + "\n")

    for t in torrents:
        name = t.get("name", "")[:40]
        state = t.get("state", "")
        category = t.get("category", "")
        save_path = t.get("save_path", "")

        line = f"{name:40} {state:12} {category:10} {save_path}\n"
        f.write(line)

    f.write("=" * 100 + "\n")
    f.write(f"Total torrents: {len(torrents)}\n")

print(f"Export complete → {output_file}")
