import os
import sys
import time
import json
import collections

def format_time():
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday
    hour = now.tm_hour
    minute = now.tm_min
    second = now.tm_sec

    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

def task_create(id, description):
    status = "todo"
    createAt = format_time()
    updatedAt = []

    return {
        "id": id,
        "description": description,
        "status": status,
        "createAt": createAt,
        "updatedAt": updatedAt
    }

def task_read(task):
    id = task.get("id")
    description = task.get("description", "")
    status = task.get("status", "todo")
    createAt = task.get("createAt", "")
    updatedAt = (task.get("updatedAt")[-1:] or [""])[0]

    return f"{id:<8d}\t{status:<15}\t{createAt:<25}\t{updatedAt:<25}\t{description}"

class TaskTracker:
    def __init__(self):
        self._path = os.path.join(os.path.abspath("."), "task.json")
        if not os.path.exists(self._path):
            with open(self._path, "w+") as file:
                json.dump({"add_id": -1, "tasks": {}}, file)
            print("No tasks.json file found, creating one...")

        # {add_id:[], tasks:{}}
        with open(self._path, "r") as file:
            data = json.load(file)

            self.odd_id = collections.deque(data.get("odd_id", []))
            self.add_id = data.get("add_id", -1)
            self.tasks = data.get("tasks", {})

    def is_exist(self, id):
        cur_task = self.tasks.get(id, [])
        if not cur_task:
            sys.exit(f"KeyError: This task doesn't exist (ID: {id})")
        return cur_task

    def new_id(self):
        if self.odd_id:
            return self.odd_id.popleft()
        else:
            self.add_id += 1
            return self.add_id

    def mark_status(self, id, status):
        cur_task = self.is_exist(id)
        cur_task.update(status=status)

    def add(self, description):
        cur_id = self.new_id()

        self.tasks.setdefault(cur_id, task_create(cur_id, description))
        print(f"Output: Task added successfully (ID:{cur_id})")

    def update(self, id, description):
        cur_task = self.is_exist(id)

        cur_update = cur_task.get("updatedAt", [])
        cur_update.append(format_time())

        cur_task.update(description=description)
        cur_task.update(updatedAt=cur_update)

        # self.tasks.update(cur_task)

    def delete(self, id):
        cur_task = self.is_exist(id)

        self.tasks.pop(id)
        self.odd_id.append(id)

    def list(self, cond):
        # id, description, status, createAt, updatedAt
        print(f"{'Id':<8}\t{'Status':<15}\t{'CreateAt':<25}\t{'uppdatedAt':<25}\tDescription")

        # condition: "done", "todo", "in-progress", "all"
        for value in self.tasks.values():
            if value.get("status") == cond or cond == "all":
                print(task_read(value))

    def mark_in_progress(self, id):
        self.mark_status(id, "in-progress")

    def mark_done(self, id):
        self.mark_status(id, "done")

    def __del__(self):
        with open(self._path, "w") as file:
            json.dump({"add_id": self.add_id, "odd_id": list(self.odd_id), "tasks": self.tasks}, file)
