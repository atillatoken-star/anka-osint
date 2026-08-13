
def analyze_email(email):
    parts = email.split("@")
    return {
        "target": email,
        "valid_format": len(parts) == 2,
        "local": parts[0] if len(parts) == 2 else None,
        "domain": parts[1] if len(parts) == 2 else None
    }
