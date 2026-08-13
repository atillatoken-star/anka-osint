from urllib.parse import urlparse

def normalize_target(target: str) -> str:
    if target.startswith(("http://", "https://")):
        return urlparse(target).netloc
    return target
