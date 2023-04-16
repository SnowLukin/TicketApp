from enum import Enum


class TaskType(Enum):
    practice = 'Practice'
    theory = 'Theory'


class Task:
    def __init__(self, task_id: int, description: str, complexity: int, task_type: TaskType):
        self.task_id = task_id
        self.description = description
        self.complexity = complexity
        self.task_type = task_type

    def __str__(self):
        return f'{self.task_type.value}, Complexity: {self.complexity}, {self.description}'

    def __lt__(self, other):
        return self.complexity < other.complexity or \
            (self.complexity == other.complexity and self.task_id < other.task_id)
