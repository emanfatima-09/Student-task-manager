# Student Task Management System - Validation & Lifecycle Module
def complete_task(task_list, task_number):
    index = task_number - 1
    if 0 <= index < len(task_list):
        done = task_list.pop(index)
        print(f"Completed task: '{done}'")
    else:
        print("Error: Invalid task index")
    return task_list

if __name__ == "__main__":
    sample_list = ["Task 1", "Task 2"]
    complete_task(sample_list, 1)