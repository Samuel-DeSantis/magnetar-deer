# Git Workflow
Git guide for collaborating on programming projects.

## Contents
1. [One-time Setup](#one-time-setup)
2. [Daily Workflow](#daily-workflow)
3. [Standard Workflow](#standard-workflow)

## ONE-TIME SETUP

### Clone the repo (download it to your computer)
`git clone <repo_url>`

### Enter the project folder
`cd <repo_name>`


## DAILY WORKFLOW

 Check current status (what changed, what’s staged, what’s not)

`git status`

### Get latest changes from GitHub (do this before working)
`git pull`

### Edit code/files in your editor

### See what changed
`git diff`

### Stage files (mark them for commit)
`git add file.py          # single file`

`git add .                # all changes`

### Save changes locally with a message
`git commit -m "Short description of what I changed"`

### Upload commits to GitHub
`git push`

### WHEN STARTING NEW WORK

Always pull first to avoid conflicts
`git pull`

### Then start coding

### IF YOU MESSED UP

### Unstage a file (undo git add)
`git reset file.py`

### Discard local changes (DANGEROUS: deletes edits)
`git checkout -- file.py`

### See commit history
`git log --oneline`

## BRANCHING (OPTIONAL, IF WE USE IT) --------

# Create and switch to new branch
`git checkout -b feature-name`

# Switch back to main
`git checkout main`

# Push branch to GitHub
`git push -u origin feature-name`


# -------- RULES --------

# 1. Pull before you start working
# 2. Commit often (small commits)
# 3. Push at least once per day
# 4. Never edit directly on GitHub unless agreed
# 5. Ask before force-pushing

## STANDARD WORKFLOW
```
git pull                  # Update your local codebase
# edit code
git status                #
git add .                 # W/ "." add ALL changes to
git commit -m "message"   #
git push                  # Push changes to remote repo
```