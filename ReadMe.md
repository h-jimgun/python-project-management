# Python Project Management CLI Tool

A Command-Line Interface (CLI) application built in Python to manage users, projects, and tasks. It features local JSON persistence, modular Object-Oriented design, and beautiful terminal output using the `rich` library.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/h-jimgun/python-project-management.git
   ```

2. Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependancies
   ```bash
   pip install -r requirements.txt
   ```

## CLI Commands
1. Add a User
   ```bash
   python main.py add-user --name "Alex" --email "alex@example.com"
   ```

2. Add a project to user
   ```bash
   python main.py add-project --user "Alex" --title "CLI Tool" --description "Build a CLI" --due_date "2026-12-01"
   ```

3. Add a Task to a project
   ```bash
   python main.py add-task --project "CLI Tool" --title "Implement add-task"
    ```

4. List Project for a User
   ```bash
   python main.py list-projects --user "Alex"
   ```

5. Complete a Task
   ```bash
   python main.py complete-task --project "CLI Tool" --task "Implement add-task"
   ```

## Features and Overview
- OOP Design: Uses Inheritance (Person -> User), Properties (@property and @setter for email validation), and Class Attributes (Project._id_counter).

- CLI Implementation: Utilizes Python's standard argparse module for subcommands.

- Persistence: Data is saved locally in data/users.json. Safely loads and handles missing files.

- External Packages: Uses rich for printing formatted tables in the terminal.

- Code Structure: Separated into models/, utils/, and main.py for clean, modular code.


