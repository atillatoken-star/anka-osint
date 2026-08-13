
import requests

def fetch_sitemap(url):
    try:
        return requests.get(url.rstrip("/") + "/sitemap.xml", timeout=10).text
    except Exception as e:
        return str(e)
