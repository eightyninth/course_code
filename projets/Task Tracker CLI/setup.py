from setuptools import setup
setup(
    name="task-cli",
    version="0.0.1",
    description="A simple task tracker",
    author="eightyninth",
    python_requires=">=3.8",
    packages=["task_cli"],
    entry_points={
        "console_scripts": [
            "task-cli = task_cli.__main__:main"
        ]
    }
)