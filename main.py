import json

# Load tasks
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

def add_task():
    task = input("Enter problem (with difficulty - easy/medium/hard): ")
    tasks.append(task)

    

    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def ai_suggestion():
    if not tasks:
        print("AI Suggestion: Start solving at least 2 problems daily.")
        return

    easy = sum(1 for t in tasks if "easy" in t.lower())
    medium = sum(1 for t in tasks if "medium" in t.lower())
    hard = sum(1 for t in tasks if "hard" in t.lower())

    print("\n--- AI Analysis ---")

    if easy > medium:
        print("You are solving many easy problems. Try medium level.")
    elif medium > hard:
        print("Good progress! Try more hard problems.")
    else:
        print("Great balance! Keep going.")

def menu():
    while True:
        print("\n=== AI Placement Preparation Tracker ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. AI Suggestion")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            ai_suggestion()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()
