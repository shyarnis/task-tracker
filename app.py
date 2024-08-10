import argparse
from cruds import create, read, update, delete


def main():
    parser = argparse.ArgumentParser(description="CLI to track and manage your tasks.")

    # Create a task
    parser.add_argument("-a", "--add", help="Add a new task with provided description.")

    # Read a task list
    parser.add_argument(
        "-l",
        "--list",
        choices=["todo", "done", "in-progress", "all"],
        help="List all tasks.",
        default=None,
        nargs="?",
        const="all",
    )

    # Update a task list
    parser.add_argument(
        "-u",
        "--update",
        nargs=2,  # specifies two arguments
        help="Update a task by providing task ID and new description.",
    )

    # delete a task
    parser.add_argument("-d", "--delete", help="Delete a task by providing a task ID.")

    # update a status by in-progress
    parser.add_argument(
        "-mip",
        "--mark-in-progress",
        help="Mark a task as 'in-progress' by providing the task ID.",
    )

    # update a status by done
    parser.add_argument(
        "-md",
        "--mark-done",
        help="Mark a task as 'done' by providing the task ID.",
    )

    args = parser.parse_args()

    # "-a" "--add"
    if args.add:
        create.add_task(args.add)

    # "-l" "--list"
    if args.list:
        read.show_list(args.list)

    # "-u" "--update"
    if args.update:
        task_id = int(args.update[0])  # by deafult <class 'str'>
        task_description = args.update[1]
        update.update_task(task_id, task_description)

    # "-d" "--delete"
    if args.delete:
        # task_id = int(args.delete[0])  <-- WARN: it will only take one digit number.
        task_id = int(args.delete)
        delete.delete_task(task_id)

    # "-mip" "-mark-in-progress"
    if args.mark_in_progress:
        # task_id = int(args.mark_in_progress[0]) <-- WARN: it will only take one digit number.
        task_id = int(args.mark_in_progress)
        update.update_status(task_id, "in-progress")

    # "-md" "-mark-done"
    if args.mark_done:
        task_id = int(args.mark_done)
        update.update_status(task_id, "done")


if __name__ == "__main__":
    main()
