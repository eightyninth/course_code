#  Task Tracker

## Get Started

### use

```bash
pip install -r requirements.txt
pip install dist/task_cli-0.0.1-py3-none-any.whl
```

### example
```bash
# add task
task-cli add "example task"
# Output: Task added successfully (ID: x)

# update task
task-cli update x "new description"

# delete task
task-cli delete x

# list task
task-cli list
task-cli list todo
task-cli list done
task-cli list in-progress
task-cli list all

# mark task
task-cli mark_done x
task-cli mark_in_progress x
```

## Implementation 

### Add Task

### Update Task

### Delete Task

### List Task
- All
- done
- in-progress
- todo

### Mark Task Condition

- done
- in-progress
- todo

## Data Structure

- id
- description
- status
- createdAt
- updatedAt

## reference
[Task Tracker](https://roadmap.sh/projects/task-tracker)
[roadmap.sh](https://roadmap.sh/)
