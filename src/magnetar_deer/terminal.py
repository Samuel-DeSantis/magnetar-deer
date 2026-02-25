import os

class Terminal:

    @classmethod
    def run(cls):
        while True:
            user_input = input("$ ")
            match user_input:
                case 'agent':
                    print('Agent chat WIP')
                case 'help':
                    cls.help()
                case 'exit' | 'quit' | 'close':
                    break
                case 'clear':
                    os.system('clear')
                case _:
                    print("> unknown command")
    
    @classmethod
    def help(cls) -> None:
        commands = {
            'exit | quit | close': 'exit and close the program',
            'agent': 'start a chat with AI NL to SQL agent',
            'clear': 'clear the terminal window',
        }

        print("Available commands:")
        # compute padding based on the longest command string
        max_cmd_len = max(len(cmd) for cmd in commands)
        for command, desc in commands.items():
            print(f"  {command.ljust(max_cmd_len)}  — {desc}")
