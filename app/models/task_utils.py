import re
from app.models.task import Task, TaskType


def generate_tasks(source: list[str], task_type: TaskType) -> list[Task]:
    pattern = r'{( )*\d+( )*}'
    tasks = []
    for index, element in enumerate(source):
        match = re.search(pattern, element)
        complexity = None
        if match:
            complexity_string = match.group(0)
            complexity = int(complexity_string[1:-1])
        description = re.sub(pattern, '', element, count=1)
        task = Task(task_id=index, description=description, task_type=task_type, complexity=complexity)
        tasks.append(task)
    return tasks


