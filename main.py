# /main.py
from datetime import date
from commands import command_list, repl_command, exit_command, help_command

def main():
    current_year = date.today().year
    
    repl_loop = True
    while repl_loop:
        user_input = input("Bible Reader > ")
        command_parts = user_input.split()
        
        if not command_parts:
            continue
        
        command_name = command_parts[0]
        args = command_parts[1:]
        
        if command_name in command_list:
            try:
                command_list[command_name].func(args)
            except Exception as e:
                print(f"Error executing command '{command_name}': {e}")
        else:
            print(f"Unknown command: '{command_name}'. Type 'help' for available commands.")

    
    
if __name__ == "__main__":
    main()