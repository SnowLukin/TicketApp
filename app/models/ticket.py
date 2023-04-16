from app.models.task import Task


class Ticket:
    def __init__(self, ticket_id: int, theory: list[Task], practice: list[Task]):
        self.ticket_id = ticket_id
        self.theory = theory
        self.practice = practice
        self.ticket_name = 'Вопросы'

    def __repr__(self):
        return f'Ticket: {self.ticket_id}'

    def complexity(self):
        return self.theory_complexity() + self.practice_complexity()

    def theory_complexity(self):
        return sum(task.complexity for task in self.theory)

    def practice_complexity(self):
        return sum(task.complexity for task in self.practice)