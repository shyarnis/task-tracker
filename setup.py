from setuptools import setup, find_packages

setup(
    name="Task Tracker CLI",
    description="A simple CLI tool to manage tasks",
    version="0.0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["task-cli=app:main"]},
)
