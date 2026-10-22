# Python Project Management CLI Tool

A Command-Line Interface (CLI) application built in Python to manage users, projects, and tasks. It features local JSON persistence, modular Object-Oriented design, and beautiful terminal output using the `rich` library.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/h-jimgun/python-project-management.git
   
   cd python-project-management
   ```

2. Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
   


## CLI Commands
1. Add a User:
   ```bash
   python main.py add-user --name "Axing" --email "axing@gmail.com"
   ```

**Project Management**

2. Add a project to user:
   ```bash
   python main.py add-project --user "Axing" --title "CLI Tool" --description "Build a CLI" --due_date "2026-12-01"
   ```

3. Update a Project Details:
   - *You can update the title, description, or due date*
   ```bash
   python main.py update-project --user "Axing" --title "CLI Tool" --new_title "Advanced CLI" --new_description "Building a complex CLI tool"  --new_due_date "2026-12-31"
   ```      

4. Delete a project:
   ```bash
   python main.py delete-project --user "Axing" --title "Advanced CLI"
   ```
  
5. List Projects for a User:
   ```bash
   python main.py list-projects --user "Axing"
   ```
 
**Task Management**

6. Add a Task to a project:
   *Tasks default to "Unassigned" if you don't use --assigned_to*
   ```bash
   python main.py add-task --user "Axing" --project "CLI Tool" --title "Implement add-task" --assigned_to "Sophie"
   ```

7. Update a Task's Title or Assignee:
   ```bash
   python main.py update-task --user "Axing" --project "CLI Tool" --old_title "Implement add-task" --new_title "Finish the code" --new_assigned_to "Maple"
   ```

8. Mark a Task as Complete:
   ```bash
   python main.py complete-task --user "Axing" --project "CLI Tool" --task "Finish the code"
   ```

9. Delete a Task:
   ```bash
   python main.py delete-task --user "Axing" --project "CLI Tool" --task "Finish the code"
   ```

## Features and Overview
- **OOP Design:** Uses Inheritance (Person -> User), Properties (@property and @setter for email validation), and Class Attributes (Project._id_counter).

- **CLI Implementation:** Utilizes Python's standard argparse module for subcommands.

- **Persistence:** Data is saved locally in data/users.json. Safely loads and handles missing files.

- **External Packages:** Uses rich for printing formatted tables in the terminal.

- **Code Structure:** Separated into models/, utils/, and main.py for clean, modular code.


