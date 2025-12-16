import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent.parent / "config.json"  # Adjust if needed


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


config = load_config()
print(config["default_save_path"])
