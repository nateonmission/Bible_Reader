import os
from pages import print_home, print_history
from datetime import datetime
from data_manager import plan, reading_history, bible_data, get_today_passage, today, passage_parser, save_reading_history, count_verses
from reading import Reading, DailyReading



class repl_command:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func
       
def clear_command(args):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
       
def exit_command(args):
    print("Exiting Bible Reader...")
    success = save_reading_history(reading_history)
    if not success:
        print("Failed to save reading history.")
    exit(0)
    
         
def help_command(args):
    print("Available commands:")
    for cmd in command_list.values():
        print(f"{cmd.name}: {cmd.description}")
        
       
def home_command(args):
    print_home(get_today_passage())
    
    
def record_command(args):
    if args[0] == "today":
        print("Recording today's passage...")
        passage = get_today_passage()
        this_reading = passage_parser(passage.split())
    else:
        this_reading = passage_parser(args)    
    if this_reading is None:
        return
    
    todays_readings = reading_history.get(today)
    if todays_readings:
        reading_history[today].readings.append(this_reading)
        success = save_reading_history(reading_history)
    else:
        new_daily_reading = DailyReading(date=today, readings=[this_reading])
        reading_history[today] = new_daily_reading
        success = save_reading_history(reading_history)
        
    if success:
        print(f"Recording reading: {reading_history[today]}")
    else:
        print("Failed to save reading history.")
    
    
def history_command(args):
    clear_command(args)
    if not reading_history:
        print("No readings recorded yet.")
        return
    
    print_history(reading_history)
    
def vcount_command(args):
    print(f"Total verses read today: {count_verses(reading_history.get(today))}")
       
       
       
       
       
       
       
       
       
       
       
        
command_list = {
    "clear": repl_command("clear", "Clear the console", clear_command),
    "exit": repl_command("exit", "Exit the REPL", exit_command),
    "help": repl_command("help", "Show this help message", help_command),
    "home": repl_command("home", "Re-prints the home screen", home_command),
    "record": repl_command("record", "Record a reading for today. Usage: record [book] [start chapter] [start verse] [end chapter] [end verse]", record_command),
    "history": repl_command("history", "Show reading history", history_command),
    "vcount": repl_command("vcount", "Show total verses read today", vcount_command)
    
}