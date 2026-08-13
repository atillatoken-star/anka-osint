
import ipaddress

def analyze_ip(ip):
    data = {"target": ip}
    try:
        obj = ipaddress.ip_address(ip)
        data["version"] = obj.version
        data["is_private"] = obj.is_private
        data["is_global"] = obj.is_global
    except Exception as e:
        data["error"] = str(e)
    return data
