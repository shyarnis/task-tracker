import os
import json
import unittest
import subprocess

TASKS_FILE = os.path.join(os.path.dirname(__file__), "..", "tasks.json")


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.test_task = [
            {
                "id": 1,
                "description": "Test Task",
                "status": "todo",
                "createdAt": "August 10, 2024 at 09:13 PM",
                "updatedAt": "August 10, 2024 at 09:13 PM",
            }
        ]
        with open(TASKS_FILE, "w") as file:
            json.dump(self.test_task, file)

    def tearDown(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def run_cli(self, *args):
        """Helper function to run the CLI and capture output."""
        result = subprocess.run(
            ["python3", os.path.join(os.path.dirname(__file__), "..", "app.py")]
            + list(args),
            capture_output=True,
            text=True,
        )
        return result

    def test_add_task(self):
        result = self.run_cli("--add", "Complete the Task")
        self.assertEqual(result.returncode, 0)

        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 2)  # new task was added
        self.assertEqual(tasks[-1]["description"], "Complete the Task")

    def test_list_tasks(self):
        result = self.run_cli("--list")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Test Task", result.stdout)

    def test_update_task(self):
        result = self.run_cli("--update", "1", "Updated Task")
        self.assertEqual(result.returncode, 0)

        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        self.assertEqual(tasks[0]["description"], "Updated Task")

    def test_delete_task(self):
        result = self.run_cli("--delete", "1")
        self.assertEqual(result.returncode, 0)

        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 0)

    def test_mark_in_progres(self):
        result = self.run_cli("--mark-in-progress", "1")
        self.assertEqual(result.returncode, 0)

        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        self.assertEqual(tasks[0]["status"], "in-progress")

    def test_mark_done(self):
        result = self.run_cli("--mark-done", "1")
        self.assertEqual(result.returncode, 0)

        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        self.assertEqual(tasks[0]["status"], "done")


if __name__ == "__main__":
    unittest.main()
