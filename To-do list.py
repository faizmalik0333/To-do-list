import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    while True:
        print("Options: [1] View [2] Add [3] Remove [4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter a task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.\n")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Removed: {removed}\n")
                else:
                    print("Invalid number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
