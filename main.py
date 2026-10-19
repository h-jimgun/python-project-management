import argparse
from rich.console import Console
from rich.table import Table
from utils.storage import load_data, save_data
from models.user import User, Project
from models.task import Task

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    
    parser_user = subparsers.add_parser("add-user", help="Add a new user")
    parser_user.add_argument("--name", required=True)
    parser_user.add_argument("--email", required=True)

   
    parser_project = subparsers.add_parser("add-project", help="Add a project to a user")
    parser_project.add_argument("--user", required=True)
    parser_project.add_argument("--title", required=True)
    parser_project.add_argument("--description", default="")
    parser_project.add_argument("--due_date", default="N/A")

    
    parser_task = subparsers.add_parser("add-task", help="Add a task to a project")
    parser_task.add_argument("--project", required=True)
    parser_task.add_argument("--title", required=True)

   
    parser_list = subparsers.add_parser("list-projects", help="List projects for a user")
    parser_list.add_argument("--user", required=True)

   
    parser_complete = subparsers.add_parser("complete-task", help="Mark a task as complete")
    parser_complete.add_argument("--project", required=True)
    parser_complete.add_argument("--task", required=True)

    args = parser.parse_args()
    users_data = load_data("users.json")

   
    if args.command == "add-user":
        try:
            new_user = User(args.name, args.email)
            users_data.append(new_user.to_dict())
            save_data("users.json", users_data)
            console.print(f"[green]Success:[/] User '{args.name}' added.")
        except ValueError as e:
            console.print(f"[red]Error:[/] {e}")

    elif args.command == "add-project":
        user_found = False
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                user_found = True
                new_proj = Project(args.title, args.description, args.due_date)
                u["projects"].append(new_proj.to_dict())
                save_data("users.json", users_data)
                console.print(f"[green]Success:[/] Project '{args.title}' added to {args.user}.")
                break
        if not user_found:
            console.print(f"[red]Error:[/] User '{args.user}' not found.")

    elif args.command == "add-task":
        for u in users_data:
            for p in u["projects"]:
                if p["title"].lower() == args.project.lower():
                    new_task = Task(args.title)
                    p["tasks"].append(new_task.to_dict())
                    save_data("users.json", users_data)
                    console.print(f"[green]Success:[/] Task '{args.title}' added to '{args.project}'.")
                    return
        console.print(f"[red]Error:[/] Project '{args.project}' not found.")

    elif args.command == "list-projects":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                table = Table(title=f"Projects for {u['name']}")
                table.add_column("Title", style="cyan")
                table.add_column("Description")
                table.add_column("Due Date", style="magenta")
                table.add_column("Tasks", style="green")
                
                for p in u["projects"]:
                    task_list = ", ".join([t["title"] for t in p["tasks"]]) if p["tasks"] else "None"
                    table.add_row(p["title"], p["description"], p["due_date"], task_list)
                
                console.print(table)
                return
        console.print(f"[red]Error:[/] User '{args.user}' not found.")

    elif args.command == "complete-task":
        for u in users_data:
            for p in u["projects"]:
                if p["title"].lower() == args.project.lower():
                    for t in p["tasks"]:
                        if t["title"].lower() == args.task.lower():
                            t["status"] = "Complete"
                            save_data("users.json", users_data)
                            console.print(f"[green]Success:[/] Task '{args.task}' marked as complete.")
                            return
        console.print(f"[red]Error:[/] Project or Task not found.")

if __name__ == "__main__":
    main()