
from urllib.parse import urlparse

def normalize_target(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://"):
        return urlparse(target).netloc
    return target
