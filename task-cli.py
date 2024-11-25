import sys
import json
import os
from datetime import datetime

# Define the file to store tasks
TASK_FILE = "tasks.json"

# Ensure the JSON file exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"Task {task_id} not found")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted successfully")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"ID: {task['id']} | Status: {task['status']} | Description: {task['description']}")

def handle_command(args):
    if args[0] == "add" and len(args) > 1:
        add_task(" ".join(args[1:]))
    elif args[0] == "update" and len(args) > 2:
        update_task(int(args[1]), " ".join(args[2:]))
    elif args[0] == "delete" and len(args) > 1:
        delete_task(int(args[1]))
    elif args[0] == "mark-in-progress" and len(args) > 1:
        mark_task(int(args[1]), "in-progress")
    elif args[0] == "mark-done" and len(args) > 1:
        mark_task(int(args[1]), "done")
    elif args[0] == "list":
        if len(args) > 1:
            list_tasks(args[1])
        else:
            list_tasks()
    else:
        print("Invalid command. Available commands: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
    else:
        handle_command(sys.argv[1:])
