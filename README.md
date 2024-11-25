Task Tracker CLI

Overview
Task Tracker CLI is a simple command-line interface (CLI) application for managing tasks. It allows you to add, update, delete, and list tasks, as well as track their statuses (todo, in-progress, done). Tasks are stored in a JSON file in the current directory, making it easy to persist and manage your tasks.

Features
- Add tasks
- Update task descriptions
- Delete tasks
- Mark tasks as **todo**, **in-progress**, or **done**
- List tasks by status or show all tasks

---

Installation

Prerequisites
- Python 3.x must be installed on your system.
- Ensure the Python `sys` and `json` modules are available (they are part of the standard library).

Steps
1. Clone or download the project repository to your local machine.
2. Navigate to the project directory in your terminal:
   ```bash
   cd <project_directory>
   ```
3. Ensure the `task-cli.py` file is executable:
   ```bash
   chmod +x task-cli.py
   ```
4. Run the CLI using Python:
   ```bash
   python task-cli.py <command>
   ```

---

Usage

General Syntax
```bash
python task-cli.py <command> [arguments]
```

Available Commands

Add a Task
```bash
python task-cli.py add "Task description"
```
**Example:**
```bash
python task-cli.py add "Buy groceries"
```
**Output:**
```
Task added successfully (ID: 1)
```

Update a Task
```bash
python task-cli.py update <task_id> "New description"
```
**Example:**
```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
```
**Output:**
```
Task 1 updated successfully
```

Delete a Task
```bash
python task-cli.py delete <task_id>
```
**Example:**
```bash
python task-cli.py delete 1
```
**Output:**
```
Task 1 deleted successfully
```

Mark a Task as In Progress
```bash
python task-cli.py mark-in-progress <task_id>
```
**Example:**
```bash
python task-cli.py mark-in-progress 1
```
**Output:**
```
Task 1 marked as in-progress
```

Mark a Task as Done
```bash
python task-cli.py mark-done <task_id>
```
**Example:**
```bash
python task-cli.py mark-done 1
```
**Output:**
```
Task 1 marked as done
```

List All Tasks
```bash
python task-cli.py list
```
**Example:**
```bash
python task-cli.py list
```
**Output:**
```
ID: 1 | Status: todo | Description: Buy groceries
```

List Tasks by Status
```bash
python task-cli.py list <status>
```
- **Statuses:** `todo`, `in-progress`, `done`

**Example:**
```bash
python task-cli.py list done
```
**Output:**
```
ID: 1 | Status: done | Description: Buy groceries
```

---

Sample Workflow

1. Add tasks:
   ```bash
   python task-cli.py add "Read a book"
   python task-cli.py add "Write a blog post"
   ```
2. List all tasks:
   ```bash
   python task-cli.py list
   ```
   **Output:**
   ```
   ID: 1 | Status: todo | Description: Read a book
   ID: 2 | Status: todo | Description: Write a blog post
   ```
3. Mark a task as in-progress:
   ```bash
   python task-cli.py mark-in-progress 1
   ```
4. Update a task description:
   ```bash
   python task-cli.py update 2 "Write a technical blog post"
   ```
5. List tasks by status:
   ```bash
   python task-cli.py list in-progress
   ```
   **Output:**
   ```
   ID: 1 | Status: in-progress | Description: Read a book
   ```
6. Delete a task:
   ```bash
   python task-cli.py delete 2
   ```

---

Notes
- The application creates a `tasks.json` file in the current directory if it does not exist.
- The JSON file is used to persist task data between sessions.

---

Future Enhancements
- Add priority levels to tasks.
- Implement due dates and reminders.
- Add task search functionality.
- Export tasks to other formats like CSV.

this is part of https://roadmap.sh/projects/task-tracker

Enjoy tracking your tasks with the Task Tracker CLI! 🎉
