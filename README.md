# magnetar-deer

## Setup

Run `pip install .`

Gemini API
Create `.../agent/agent.env`

```
# /agent.env
GEMINI_API_KEY=<YOUR API KEY HERE>
```

## Project Short-term Goals
Prompt-Action Goal
Prompt: "I want to track my workouts to record the name of the workout, the weight used or duration, and any notes I might have, + date and time if provided."
Action: Create "Workout" table with Name:string, Weight:Int, Duration:Int, Notes:string
Prompt: "Today I benched 135lb, and squated 225lbs, and my knee felt a little funny."

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

How much power does the agent have?
    - Can the agent execute code? Does the agent only parse the code.

## Draft Structure
magnetar-deer
|--main.py
|--/db #SQLalchemy
|----models
|----engine.py
|---- ...
|--/controller
|----users_controller.py # Create, Read, Update, Delete
|----xxxx_controller.py
|--/agent
|----agent.py
|----constraints.py/formatting 

```
# ============================================================
# BASIC GIT WORKFLOW (FOR THIS PROJECT)
# ============================================================

# -------- ONE-TIME SETUP --------

# Clone the repo (download it to your computer)
git clone <repo_url>

# Enter the project folder
cd <repo_name>


# -------- DAILY WORKFLOW --------

# Check current status (what changed, what’s staged, what’s not)
git status

# Get latest changes from GitHub (do this before working)
git pull

# Edit code/files in your editor

# See what changed
git diff

# Stage files (mark them for commit)
git add file.py          # single file
git add .                # all changes

# Save changes locally with a message
git commit -m "Short description of what I changed"

# Upload commits to GitHub
git push


# -------- WHEN STARTING NEW WORK --------

# Always pull first to avoid conflicts
git pull

# Then start coding


# -------- IF YOU MESSED UP --------

# Unstage a file (undo git add)
git reset file.py

# Discard local changes (DANGEROUS: deletes edits)
git checkout -- file.py

# See commit history
git log --oneline


# -------- BRANCHING (OPTIONAL, IF WE USE IT) --------

# Create and switch to new branch
git checkout -b feature-name

# Switch back to main
git checkout main

# Push branch to GitHub
git push -u origin feature-name


# -------- RULES --------

# 1. Pull before you start working
# 2. Commit often (small commits)
# 3. Push at least once per day
# 4. Never edit directly on GitHub unless agreed
# 5. Ask before force-pushing

# -------- STANDARD WORKFLOW --------

# git pull
# edit code
# git status
# git add .
# git commit -m "message"
# git push
```