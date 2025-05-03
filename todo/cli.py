import argparse
import json
import os
import sys
from typing import List, Dict, Any

TASKS_FILE = "tasks.json"

def load_tasks(file_path: str = TASKS_FILE) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks: List[Dict[str, Any]], file_path: str = TASKS_FILE) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(description: str) -> None:
    tasks = load_tasks()
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "description": description, "done": False})
    save_tasks(tasks)
    print(f"Added task {next_id}: {description}")

def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        status = "x" if task.get("done") else " "
        print(f"{task['id']}. [{status}] {task['description']}")

def mark_done(task_id: int) -> None:
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task.get("done"):
                print(f"Task {task_id} is already done.")
            else:
                task["done"] = True
                save_tasks(tasks)
                print(f"Marked task {task_id} as done.")
            return
    print(f"No task with id {task_id}.")
    sys.exit(1)

def delete_task(task_id: int) -> None:
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task with id {task_id}.")
        sys.exit(1)
    save_tasks(new_tasks)
    print(f"Deleted task {task_id}.")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="todo", description="Simple Todo CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_add = subparsers.add_parser("add", help="Add a new task")
    p_add.add_argument("description", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    p_done = subparsers.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int, help="Task ID")

    p_delete = subparsers.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id", type=int, help="Task ID")

    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        print("Unknown command")
        sys.exit(1)
