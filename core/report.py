from pathlib import Path
from datetime import datetime
import json

def save_json(data, target):
    Path("reports/json").mkdir(parents=True, exist_ok=True)

    filename = Path("reports/json") / f"{target}_{datetime.now():%Y%m%d_%H%M%S}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return filename
