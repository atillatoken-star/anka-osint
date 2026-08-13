
import whois

def lookup(domain):
    try:
        w = whois.whois(domain)
        return {
            "registrar": getattr(w, "registrar", None),
            "creation_date": str(getattr(w, "creation_date", None)),
            "expiration_date": str(getattr(w, "expiration_date", None)),
        }
    except Exception as e:
        return {"error": str(e)}
