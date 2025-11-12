import json
from pathlib import Path

APP_CONFIG = Path("app_config.json")

def load_config():
    if not APP_CONFIG.exists():
        default = {"theme": "light", "version": "1.0"}
        save_config(default)
        return default
    with open(APP_CONFIG, "r") as file:
        return json.load(file)

def save_config(data):
    with open(APP_CONFIG, "w") as file:
        json.dump(data, file, indent=4)