
import os
from rich import print
from rich.console import Console

from data_manager import reading_history, today, count_verses


from datetime import datetime, timedelta
from rich.table import Table
from rich.console import Console


DARK_BLUE = "#001b44"
GOLD = "#ffd700"


def block_for_count(count):
    if count >= 25:
        return "█"
    if count == 24:
        return "▓"
    if count >= 12:
        return "▒"
    if count >= 1:
        return "░"
    return " "

def sunday_first_index(d):
    return (d.weekday() + 1) % 7

def build_heatmap(reading_history, days=91):
    console = Console()

    today = datetime.now().date()
    start_date = today - timedelta(days=days - 1)

    # number of weeks (columns)
    weeks = (days + 6) // 7

    table = Table.grid(padding=(0, 1))
    
    # add columns (weeks)
    for _ in range(weeks):
        table.add_column()

    # prepare 7 rows (Sun → Sat)
    grid = [[" " for _ in range(weeks)] for _ in range(7)]

    for i in range(days):
        current = start_date + timedelta(days=i)

        col = i // 7
        row = sunday_first_index(current)

        daily = reading_history.get(current.strftime("%Y-%m-%d"))

        if daily:
            count = count_verses(daily)
        else:
            count = 0

        grid[row][col] = block_for_count(count)

    # add rows to table
    for row in grid:
        styled_row = [
            f"[{GOLD}]{cell}[/{GOLD}]"
            for cell in row
        ]
        table.add_row(*styled_row)

    console.print(table)




def print_home(today_passage):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
    
    console = Console()
    
    
    
    console.print("[bold magenta]Welcome to the Bible Reader![/bold magenta]")
    console.print("Type [bold cyan]help[/bold cyan] to see available commands.")
    console.print("")
    build_heatmap(reading_history)
    console.print("")
    console.print(f"[yellow]Today's Passage:[/yellow] [green]{today_passage}[/green]")
    
    
def print_history(reading_history):
    console = Console()
    console.print("[bold magenta]Reading History[/bold magenta]")
    console.print("")
    for date, daily_reading in reading_history.items():
        console.print(f"[yellow]Date:[/yellow] [green]{date}[/green]")
        for reading in daily_reading.readings:
            console.print(f"        [cyan]{reading.recompose()}[/cyan]")
        console.print(f"        [bold blue]Total Verses:[/bold blue] [blue]{count_verses(daily_reading)}[/blue]")