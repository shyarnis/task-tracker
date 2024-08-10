import datetime

from utils.task_handler import initialize_file
from utils.task_handler import load_tasks
from utils.task_handler import save_tasks
from utils.datetime_readable import format_timestamp


def add_task(description: str) -> None:
    """
    Adds a new task with the specified description to the task list.

    Parameters:
        description (str): A description of the task to be added.

    Example:
        >>> add_task("submit report")
    """
    initialize_file()
    tasks = load_tasks()

    # Find the maximum ID currently in use to assign unique ID.
    max_id: int = max([task["id"] for task in tasks], default=0)

    new_task = {
        "id": max_id + 1,
        "description": description,
        "status": "todo",
        "createdAt": format_timestamp(datetime.datetime.now()),
        "updatedAt": format_timestamp(datetime.datetime.now()),
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")
