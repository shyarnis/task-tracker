import datetime

from utils.task_handler import load_tasks, save_tasks
from utils.datetime_readable import format_timestamp


def update_task(task_id: int, task_description: str) -> None:
    """
    Updates the description of a task with the specified ID.

    Parameters:
        task_id (int): The ID of the task to update.
        task_description (str): The new description for the task.

    Example:
        >>> update_task(1, "subit report")
        # Updates the description of the task ID 1 to "submit report".
    """
    tasks = load_tasks()

    # find and update task
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = task_description
            task["updatedAt"] = format_timestamp(datetime.datetime.now())
            break

    else:
        print(f"Task ID {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task updated successfully (ID: {task_id})")


def update_status(task_id: int, task_status: str) -> None:
    """
    Updates the status of a task with the specified ID.

    Parameters:
        task_id (int): The ID of the task to update.
        task_status (str): The new status for the task.

    Example:
        >>> update_task(1, "done")
        # Updates the status of the task ID 1 to "done".
    """
    tasks = load_tasks()

    # find and update task
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_status
            task["updatedAt"] = format_timestamp(datetime.datetime.now())
            break

    else:
        print(f"Task ID {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task status updated successfully (ID: {task_id})")
