from pages import print_home
import datetime
from data_manager import load_data

loaded_data = load_data(datetime.datetime.now().year)
today_datetime = datetime.datetime.now().date()
today = "2026-05-04"#today_datetime.strftime("%Y-%m-%d")
# Check if plan exists AND if 'today' is a valid key within it
plan = loaded_data.get("reading_plan")

if plan and today in plan:
    today_passage_json = plan.get(today)
    today_passage = f"{today_passage_json['book']} {today_passage_json['start chapter']}:{today_passage_json['start verse']} - {today_passage_json['end chapter']}:{today_passage_json['end verse']}"
else:
    today_passage = "Passage Not Available."
    
    
    

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
    print_home(today_passage)
       
       
       
       
       
       
       
       
       
       
       
       
        
command_list = {
    "exit": repl_command("exit", "Exit the REPL", exit_command),
    "help": repl_command("help", "Show this help message", help_command),
    "home": repl_command("home", "Re-prints the home screen", home_command)
    
}