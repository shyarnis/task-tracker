import os
import json
from typing import List, Dict

# Path to the tasks.json file, located one directory up from the current directory
TASKS_FILE: str = os.path.join(os.path.dirname(__file__), "..", "tasks.json")


def initialize_file() -> None:
    """
    Initialize the tasks file if it doesn't exist.
    Creates an empty JSON file with an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)


def load_tasks() -> List[Dict]:
    """
    Load tasks from the JSON file.

    :rtype: List[Dict] A list of task dictionaries.
    """
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks: List[Dict]) -> None:
    """
    Save tasks to the JSON file.

    :param list[Dict]: A list of task dictionaries to be saved.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
