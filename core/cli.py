from rich.console import Console
from rich.prompt import Prompt

from core.banner import show_banner
from core.report import save_json
from core.html_report import generate_html

from modules.domain import analyze_domain

console = Console()

def run():
    show_banner()

    console.print("[1] Domain Analizi")
    console.print("[0] Çıkış")

    choice = Prompt.ask("Seçim", choices=["1", "0"])

    if choice == "0":
        console.print("[yellow]Çıkılıyor...[/yellow]")
        return

    target = Prompt.ask("Domain veya URL")

    console.print("[cyan]Analiz başlatıldı...[/cyan]")

    result = analyze_domain(target)

    json_path = save_json(result, target.replace(".", "_"))
    html_path = generate_html(result)

    console.print()
    console.print(f"[green]JSON raporu:[/green] {json_path}")
    console.print(f"[green]HTML raporu:[/green] {html_path}")
