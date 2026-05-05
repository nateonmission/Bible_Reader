
import os
from rich import print
from rich.console import Console







def print_home(today_passage):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
    
    console = Console()
    
    
    
    console.print("[bold magenta]Welcome to the Bible Reader![/bold magenta]")
    console.print("Type [bold cyan]help[/bold cyan] to see available commands.")
    console.print("")
    console.print("")
    console.print("")
    console.print(f"[yellow]Today's Passage:[/yellow] [green]{today_passage}[/green]")