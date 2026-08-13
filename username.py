
def analyze_username(username):
    return {
        "target": username,
        "length": len(username),
        "has_number": any(c.isdigit() for c in username),
        "has_underscore": "_" in username
    }
