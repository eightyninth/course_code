import argparse
import sys

from task_cli.Task_Tracker import TaskTracker

def main():
    task_tracker = TaskTracker()
    parser = argparse.ArgumentParser(prog="Task Tracker", description="A simple task tracker", epilog="Example: task-cli add 'my task'")

    subparsers = parser.add_subparsers(title="Task Tracker", dest="func", required=True)

    # "add", "update", "delete", "list", "mark-in-progress", "mark-done"
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    update_parser = subparsers.add_parser("update", help="Update a task by id")
    update_parser.add_argument("id", type=str, help="Description of the task")
    update_parser.add_argument("description", help="Find task by id for update")

    delete_parser = subparsers.add_parser("delete", help="Delete a task by id")
    delete_parser.add_argument("id", type=str, help="Find task by id for delete")

    list_parser = subparsers.add_parser("list", help="List all tasks or list tasks by status")
    list_parser.add_argument("status", nargs="?", default="all", choices=["done", "todo", "in-progress", "all"], help="List tasks by status")

    mark_in_progress_parser = subparsers.add_parser("mark_in_progress", help="Mark a task as in progress")
    mark_in_progress_parser.add_argument("id", type=str, help="Find task by id for mark as in progress")

    mark_done_parser = subparsers.add_parser("mark_done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=str, help="Find task by id for mark as done")

    args = parser.parse_args()

    if args.func == "add":
        task_tracker.add(args.description)
    elif args.func == "update":
        task_tracker.update(args.id, args.description)
    elif args.func == "delete":
        task_tracker.delete(args.id)
    elif args.func == "list":
        task_tracker.list(args.status)
    elif args.func == "mark_in_progress":
        task_tracker.mark_in_progress(args.id)
    elif args.func == "mark_done":
        task_tracker.mark_done(args.id)
    else:
        sys.exit(f"ValueError: This CLI doesn't supported {args.func}")

if __name__ == "__main__":
    main()