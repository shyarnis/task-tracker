from utils.task_handler import load_tasks, save_tasks


def delete_task(task_id: int) -> None:
    """
    Deletes a task with the specified ID from the task list.

    Parameters:
        task_id (int): The ID of the task to delete.

    Example:
        >>> delete_task(1)
        # Deletes the task with ID 1 from the task list.
    """

    tasks = load_tasks()
    task_found = False

    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            task_found = True
            break

    if not task_found:
        print(f"Task ID {task_id} not found")
        return

    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")
