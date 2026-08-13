import ssl
import socket

def get_ssl_info(host):
    try:
        context = ssl.create_default_context()

        with context.wrap_socket(
            socket.socket(),
            server_hostname=host
        ) as s:

            s.settimeout(5)
            s.connect((host, 443))

            cert = s.getpeercert()

            return {
                "subject": cert.get("subject"),
                "issuer": cert.get("issuer"),
                "version": cert.get("version"),
                "not_before": cert.get("notBefore"),
                "not_after": cert.get("notAfter"),
                "serial_number": cert.get("serialNumber")
            }

    except Exception as e:
        return {"error": str(e)}
