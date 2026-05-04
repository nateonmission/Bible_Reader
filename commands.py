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
       
       
       
       
       
       
       
       
       
       
       
       
       
        
command_list = {
    "exit": repl_command("exit", "Exit the REPL", exit_command),
    "help": repl_command("help", "Show this help message", help_command)
    
}