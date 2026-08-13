import dns.resolver

def get_dns_records(domain):
    records = {}

    for rtype in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(a) for a in answers]
        except Exception:
            records[rtype] = []

    return records
