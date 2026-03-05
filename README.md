# magnetar-deer
Natural Language (NL) to SQL agent.

## Contents
- [Setup](#setup)
- [How to](#how-to-run-the-entire-program)
- [Project Short-term Goals](#project-short-term-goals)
- [Structure](#structure)
- [Resources](#resources)
## Setup
1. Install all dependencies with: `pip install -e .`
    
    __NOTE:__ ` -e` enables *editable* mode and doesn't create a packaged `/build` folder and using `.` looks at the dependencies listed in `pyproject.toml` for the project setup. See: `dependencies` and `dev` to see what is currently added
2. 

Create `.env` file in ROOT dir for Gemini API key.
```
GEMINI_API_KEY=<YOUR API KEY HERE>
```

## How to run the program
- Run `magnetar-deer` from the root of the project. It will execute everything in `../magnetar_deer/main.py`
- If you want to play around with the Gemini agent run `python3 src/magnetar_deer/agent/playground.test.py` from root

See `pyproject.toml #=> [project.scripts]`

## Structure
```
magnetar-deer
    .env                # API Keys
    .gitignore          # Files not to be added to repo
    LICENSE
    pyproject.toml      # Project Setup
    README.md
    GIT_WORKFLOW.md     # Git command helper doc
    /src
        /magnetar_deer
            /agent
                __init__.py
                instructions.py
                parser.py
                planner.py
            /controller
                __init__.py
                db_controller.py    # Interfaces with Database
            /db
                __init__.py
                engine.py           # Initialize Database
                table_builder.py    # Dynamically create tables
                utils.py
            __init__.py
            __main__.py
            main.py
            terminal.py             # Terminal user interface

```

## Project Short-term Goals
Prompt-Action Goal
Prompt: "I want to track my workouts to record the name of the workout, the weight used or duration, and any notes I might have, + date and time if provided."
Action: Create "Workout" table with Name:string, Weight:Int, Duration:Int, Notes:string
Prompt: "Today I benched 135lb, and squated 225lbs, and my knee felt a little funny."

```
{
    'prompt': <user provided prompt>,
    'reponse': {
        'parsed': <The agent parsed values>{
            'table': 'Workout',
            'record': {
                'name': 'bench',
                'weight': 225,
                ...
            }
        }
    }
}
```

How much power does the agent have?
    - Can the agent execute code? Does the agent only parse the code.

## Resources
[Git Workflow](GIT_WORKFLOW.md)