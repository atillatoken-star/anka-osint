
from rich.console import Console
from rich.prompt import Prompt
from core.banner import banner
from core.report import save_json
from modules.domain import analyze_domain
from modules.ip import analyze_ip
from modules.email import analyze_email
from modules.username import analyze_username

console = Console()

def run():
    banner()
    console.print("[1] Domain")
    console.print("[2] IP")
    console.print("[3] E-posta")
    console.print("[4] Kullanıcı adı")
    secim = Prompt.ask("Seçim", choices=["1","2","3","4"], default="1")

    if secim == "1":
        target = Prompt.ask("Domain")
        result = analyze_domain(target)
    elif secim == "2":
        target = Prompt.ask("IP")
        result = analyze_ip(target)
    elif secim == "3":
        target = Prompt.ask("E-posta")
        result = analyze_email(target)
    else:
        target = Prompt.ask("Kullanıcı adı")
        result = analyze_username(target)

    path = save_json(result, target.replace(".", "_").replace("@", "_"))
    console.print(f"[green]Kaydedildi:[/green] {path}")
