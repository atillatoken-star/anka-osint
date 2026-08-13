import requests

def get_robots(url):
    try:
        response = requests.get(
            url.rstrip("/") + "/robots.txt",
            timeout=10
        )

        return {
            "status_code": response.status_code,
            "content": response.text[:10000]
        }

    except Exception as e:
        return {"error": str(e)}
