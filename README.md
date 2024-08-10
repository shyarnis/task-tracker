# Task Tracker

Task tracker is a command line interfaces used to track and manage your tasks. This application allows you to add, update, delete and list tasks as well as mark tasks as `in-progress`, `done` or `todo`. The tasks are stored in JSON file.

## Installation Guide

Follow these steps to run the project locally.

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package installer)

### Steps

1. Clone the Repository

    ```bash
    git clone https://github.com/shyarnis/task-tracker.git
    cd task-tracker
    ```

2. Install the package
    ```bash
    pip install -e .
    ```

## Example Usage

### Add a task

```bash
task-cli --add "Complete the task"
# Output: Task added successfully (ID: 1)
```

### Update a task

```bash
task-cli --update 1 "Complete the report"
# Output: Task updated successfully (ID: 1)
```

### Update a task status

```bash
task-cli --mark-in-progress 1
# Output: Task status updated successfully (ID: 1)
```

```bash
task-cli --mark-done 1
# Output: Task status updated successfully (ID: 1)
```

### List all tasks

```bash
task-cli --list
# Output:
# ID: 1    Status: done    Description: Complete the report
```

Similarly, task listing can be done by status

```bash
task-cli --list done
# Output: Compelete the report
```

```bash
task-cli --list todo
```

```bash
task-cli --list in-progress
```

### Delete a task

```bash
task-cli --delete 1
# Output: Task deleted successfully (ID: 1)
```

## Uninstall

```bash
pip uninstall task-cli
```
