
import ssl
import socket

def ssl_info(host):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(5)
            s.connect((host, 443))
            cert = s.getpeercert()
            return {"subject": cert.get("subject"), "issuer": cert.get("issuer")}
    except Exception as e:
        return {"error": str(e)}
