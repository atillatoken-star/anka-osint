
import requests

def fetch_robots(url):
    try:
        return requests.get(url.rstrip("/") + "/robots.txt", timeout=10).text
    except Exception as e:
        return str(e)
