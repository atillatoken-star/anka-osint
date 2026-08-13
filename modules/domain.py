import socket

from core.utils import normalize_target
from modules.dns import get_dns_records
from modules.whois import get_whois
from modules.headers import get_headers
from modules.ssl import get_ssl_info
from modules.robots import get_robots
from modules.sitemap import get_sitemap

def analyze_domain(target):
    domain = normalize_target(target)

    result = {
        "target": domain
    }

    try:
        result["ip"] = socket.gethostbyname(domain)
    except Exception as e:
        result["ip_error"] = str(e)

    result["dns"] = get_dns_records(domain)
    result["whois"] = get_whois(domain)
    result["headers"] = get_headers(f"https://{domain}")
    result["ssl"] = get_ssl_info(domain)
    result["robots"] = get_robots(f"https://{domain}")
    result["sitemap"] = get_sitemap(f"https://{domain}")

    return result
