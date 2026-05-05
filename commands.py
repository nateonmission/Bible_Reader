from pages import print_home
from datetime import datetime
from data_manager import plan, reading_history, bible_data, get_today_passage, today, passage_parser
from reading import Reading, DailyReading


class repl_command:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func
       
       
       
def exit_command(args):
    print("Exiting Bible Reader...")
    exit(0)
    
         
def help_command(args):
    print("Available commands:")
    for cmd in command_list.values():
        print(f"{cmd.name}: {cmd.description}")
        
       
def home_command(args):
    print_home(get_today_passage())
    
    
def record_command(args):
    this_reading = passage_parser(args)    
    todays_readings = reading_history.get(today)
    if todays_readings:
        reading_history[today].readings.append(this_reading)
    else:
        new_daily_reading = DailyReading(date=today, readings=[this_reading])
        reading_history[today] = new_daily_reading
    print(f"Recording reading: {reading_history[today]}")
       
       
       
       
       
       
       
       
       
       
       
       
        
command_list = {
    "exit": repl_command("exit", "Exit the REPL", exit_command),
    "help": repl_command("help", "Show this help message", help_command),
    "home": repl_command("home", "Re-prints the home screen", home_command),
    "record": repl_command("record", "Record a reading for today. Usage: record [book] [start chapter] [start verse] [end chapter] [end verse]", record_command)
    
}