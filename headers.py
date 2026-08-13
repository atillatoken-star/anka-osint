
import requests

def fetch_headers(url):
    try:
        r = requests.get(url, timeout=10)
        return dict(r.headers)
    except Exception as e:
        return {"error": str(e)}
