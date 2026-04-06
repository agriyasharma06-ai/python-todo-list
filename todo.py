import json
import os
from datetime import datetime

FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:\n")
    for i, task in enumerate(tasks):
        status = "✔ Completed" if task["done"] else "❌ Pending"
        print(f"{i+1}. {task['task']} | Priority: {task['priority']} | {status}")

# Add task
def add_task(tasks):
    task_name = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")

    tasks.append({
        "task": task_name,
        "priority": priority,
        "done": False,
        "created_at": str(datetime.now())
    })

    print("Task added!")

# Complete task
def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to complete: ")) - 1
        tasks[num]["done"] = True
        print("Task marked as completed.")
    except:
        print("Invalid task number.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(num)
        print(f"Deleted task: {removed['task']}")
    except:
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== SMART TO DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
