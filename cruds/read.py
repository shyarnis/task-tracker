from utils.task_handler import load_tasks


def show_list(choice: str) -> None:
    """
    Display tasks from the task list based on the choice.

    Parameters:
        choice (str): Accepted choices "todo", "done" or "in-progress".
                        Default choice is "all".

    Example:
        >>> show_list("todo")
        # Print descriptions of task with status "todo".
    """
    tasks = load_tasks()

    if choice == "todo":
        for task in tasks:
            if task["status"] == "todo":
                print(task["description"])

    elif choice == "in-progress":
        for task in tasks:
            if task["status"] == "in-progress":
                print(task["description"])

    elif choice == "done":
        for task in tasks:
            if task["status"] == "done":
                print(task["description"])

    else:
        for task in tasks:
            print(
                f"ID: {task['id']}\t Status: {task['status']}\t Description: {task['description']}"
            )
