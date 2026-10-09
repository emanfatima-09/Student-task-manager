# Student Task Management System - View Module
tasks = ["Study for OS exam", "Complete Git lab assignment"]

def view_tasks():
    print("\n--- Current Student Tasks ---")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

if __name__ == "__main__":
    view_tasks()