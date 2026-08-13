
from pathlib import Path
from datetime import datetime
import json

def save_json(data, name):
    Path("reports").mkdir(exist_ok=True)
    path = Path("reports") / f"{name}_{datetime.now():%Y%m%d_%H%M%S}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path
