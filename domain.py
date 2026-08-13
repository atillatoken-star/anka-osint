
import socket
from core.utils import normalize_target

def analyze_domain(target):
    domain = normalize_target(target)
    data = {"target": domain}
    try:
        data["ip"] = socket.gethostbyname(domain)
    except Exception as e:
        data["ip_error"] = str(e)
    return data
