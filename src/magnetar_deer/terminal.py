import os

class Terminal:
    """
    A terminal interface for interacting with the magnetar-deer application.
    This class provides a command-line interface that allows users to execute various
    commands within an interactive loop. It handles user input, command routing, and
    provides help documentation for available commands.

    Commands:
        - agent: Start a chat with an AI natural language to SQL agent
        - help: Display all available commands with descriptions
        - exit/quit/close: Exit and close the program
        - clear: Clear the terminal window

    Example:
        >>> Terminal.run()
        $ help
        Available commands:
          exit | quit | close  — exit and close the program
          agent                — start a chat with AI NL to SQL agent
          clear                — clear the terminal window
    """

    @classmethod
    def run(cls):
        """
        Method to run the terminal application
        """
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
        """
        Help command to display available commands

        commands = {
            'exit | quit | close': 'exit and close the program',
            'agent': 'start a chat with AI NL to SQL agent',
            'clear': 'clear the terminal window',
        }
        """
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
