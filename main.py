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

    p1 = subparsers.add_parser("add-user")
    p1.add_argument("--name", required=True)
    p1.add_argument("--email", required=True)

    p2 = subparsers.add_parser("add-project")
    p2.add_argument("--user", required=True)
    p2.add_argument("--title", required=True)
    p2.add_argument("--description", default="")
    p2.add_argument("--due_date", default="N/A")

    p3 = subparsers.add_parser("update-project")
    p3.add_argument("--user", required=True)
    p3.add_argument("--title", required=True)
    p3.add_argument("--new_title")
    p3.add_argument("--new_description")
    p3.add_argument("--new_due_date")

    p4 = subparsers.add_parser("add-task")
    p4.add_argument("--user", required=True)
    p4.add_argument("--project", required=True)
    p4.add_argument("--title", required=True)
    p4.add_argument("--assigned_to", default="Unassigned")

    p5 = subparsers.add_parser("update-task")
    p5.add_argument("--user", required=True)
    p5.add_argument("--project", required=True)
    p5.add_argument("--old_title", required=True)
    p5.add_argument("--new_title", required=True)
    p5.add_argument("--new_assigned_to")

    p6 = subparsers.add_parser("complete-task")
    p6.add_argument("--user", required=True)
    p6.add_argument("--project", required=True)
    p6.add_argument("--task", required=True)

    p7 = subparsers.add_parser("delete-task")
    p7.add_argument("--user", required=True)
    p7.add_argument("--project", required=True)
    p7.add_argument("--task", required=True)

    p8 = subparsers.add_parser("delete-project")
    p8.add_argument("--user", required=True)
    p8.add_argument("--title", required=True)

    p9 = subparsers.add_parser("list-projects")
    p9.add_argument("--user", required=True)

    args = parser.parse_args()
    users_data = load_data("users.json")

    if args.command == "add-user":
        for u in users_data:
            if u["name"].lower() == args.name.lower() or u["email"].lower() == args.email.lower():
                console.print(f"[red]Error:[/] User already exists.")
                return
        try:
            users_data.append(User(args.name, args.email).to_dict())
            save_data("users.json", users_data)
            console.print(f"[green]Success:[/] User '{args.name}' added.")
        except ValueError as e:
            console.print(f"[red]Error:[/] {e}")

    elif args.command == "add-project":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.title.lower():
                        console.print(f"[red]Error:[/] Project already exists.")
                        return
                
                highest_id = max([p.get("id", 0) for p in u["projects"]] + [0])
                new_id = highest_id + 1
                
                new_proj = Project(args.title, args.description, args.due_date, project_id=new_id)
                u["projects"].append(new_proj.to_dict())
                save_data("users.json", users_data)
                console.print(f"[green]Success:[/] Project '{args.title}' added (ID: {new_id}).")
                return
        console.print(f"[red]Error:[/] User '{args.user}' not found.")

    elif args.command == "update-project":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.title.lower():
                        if args.new_title: p["title"] = args.new_title
                        if args.new_description: p["description"] = args.new_description
                        if args.new_due_date: p["due_date"] = args.new_due_date
                        save_data("users.json", users_data)
                        console.print(f"[green]Success:[/] Project updated.")
                        return
                console.print(f"[red]Error:[/] Project not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "add-task":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.project.lower():
                        for t in p["tasks"]:
                            if t["title"].lower() == args.title.lower():
                                console.print(f"[red]Error:[/] Task already exists.")
                                return
                        
                        new_task = Task(args.title, assigned_to=args.assigned_to)
                        p["tasks"].append(new_task.to_dict())
                        save_data("users.json", users_data)
                        console.print(f"[green]Success:[/] Task added.")
                        return
                console.print(f"[red]Error:[/] Project not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "update-task":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.project.lower():
                        for t in p["tasks"]:
                            if t["title"].lower() == args.old_title.lower():
                                if args.new_title: 
                                    t["title"] = args.new_title
                                if args.new_assigned_to:
                                    t["assigned_to"] = args.new_assigned_to
                                save_data("users.json", users_data)
                                console.print(f"[green]Success:[/] Task updated.")
                                return
                console.print(f"[red]Error:[/] Task not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "complete-task":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.project.lower():
                        for t in p["tasks"]:
                            if t["title"].lower() == args.task.lower():
                                t["status"] = "Complete"
                                save_data("users.json", users_data)
                                console.print(f"[green]Success:[/] Task '{args.task}' marked complete.")
                                return
                        console.print(f"[red]Error:[/] Task '{args.task}' not found.")
                        return
                console.print(f"[red]Error:[/] Project '{args.project}' not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "delete-task":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for p in u["projects"]:
                    if p["title"].lower() == args.project.lower():
                        for i in range(len(p["tasks"])):
                            if p["tasks"][i]["title"].lower() == args.task.lower():
                                del p["tasks"][i]
                                save_data("users.json", users_data)
                                console.print(f"[green]Success:[/] Task deleted.")
                                return
                console.print(f"[red]Error:[/] Task not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "delete-project":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                for i in range(len(u["projects"])):
                    if u["projects"][i]["title"].lower() == args.title.lower():
                        del u["projects"][i]
                        save_data("users.json", users_data)
                        console.print(f"[green]Success:[/] Project deleted.")
                        return
                console.print(f"[red]Error:[/] Project not found.")
                return
        console.print(f"[red]Error:[/] User not found.")

    elif args.command == "list-projects":
        for u in users_data:
            if u["name"].lower() == args.user.lower():
                table = Table(title=f"Projects for {u['name']}")
                table.add_column("ID", style="dim")
                table.add_column("Title", style="cyan")
                table.add_column("Description")
                table.add_column("Due Date", style="magenta")
                table.add_column("Tasks", style="green")
                table.add_column("Assigned To", style="yellow")
                
                for p in u["projects"]:
                    if p["tasks"]:
                        task_list = "\n".join([f"{t['title']} ({t['status']})" for t in p["tasks"]])
                        assigned_list = "\n".join([t.get('assigned_to', 'Unassigned') for t in p["tasks"]])
                    else:
                        task_list = "None"
                        assigned_list = "-"

                    table.add_row(str(p.get("id", "N/A")), p["title"], p["description"], p["due_date"], task_list, assigned_list)
                
                console.print(table)
                return
        console.print(f"[red]Error:[/] User not found.")

if __name__ == "__main__":
    main()