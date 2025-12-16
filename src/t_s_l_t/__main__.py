import requests
import csv
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
csv_file = "torrent_save_locations.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Header
    writer.writerow([
        "Name",
        "State",
        "Category",
        "Progress (%)",
        "Size (GB)",
        "Save Path"
    ])

    # Rows
    for t in torrents:
        writer.writerow([
            t.get("name", ""),
            t.get("state", ""),
            t.get("category", ""),
            round(t.get("progress", 0) * 100, 2),
            round(t.get("size", 0) / (1024 ** 3), 2),
            t.get("save_path", "")
        ])

print(f"CSV export complete → {csv_file}")
print(f"Total torrents exported: {len(torrents)}")
