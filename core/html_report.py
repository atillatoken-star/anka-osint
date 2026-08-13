from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def generate_html(data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    html = template.render(
        target=data.get("target", "-"),
        ip=data.get("ip", "-"),
        registrar=data.get("whois", {}).get("registrar", "-"),
        ssl_status="Aktif" if data.get("ssl") else "Yok",
        dns_json=data.get("dns", {}),
        headers_json=data.get("headers", {}),
        generated_at=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    )

    out_dir = Path("reports/html")
    out_dir.mkdir(parents=True, exist_ok=True)

    output = out_dir / f"{data['target']}.html"
    output.write_text(html, encoding="utf-8")

    return output
