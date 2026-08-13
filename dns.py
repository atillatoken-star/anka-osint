
import dns.resolver

def resolve_records(domain):
    result = {}
    for rtype in ["A","AAAA","MX","NS","TXT"]:
        try:
            result[rtype] = [str(r) for r in dns.resolver.resolve(domain, rtype)]
        except Exception:
            result[rtype] = []
    return result
