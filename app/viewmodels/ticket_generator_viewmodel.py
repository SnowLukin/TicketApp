import os

from app.models.task import TaskType
from app.models.task_utils import generate_tasks
from app.models.ticket_generator import Generator
from utils.docx_utils import generate_docx
from utils.docx_parser import extract_theory, extract_practice


class TicketGeneratorViewModel:
    def __init__(self):
        self.theory_tasks = []
        self.practice_tasks = []
        self.ticket_amount = 0
        self.theory_count = 0
        self.practice_count = 0
        self.include_none_complexity = False

    def select_theory_file(self, file_name: str):
        text = extract_theory(file_name)
        self.theory_tasks = generate_tasks(text, TaskType.theory)

    def select_practice_file(self, file_name: str):
        text = extract_practice(file_name)
        self.practice_tasks = generate_tasks(text, TaskType.practice)

    def generate_tickets(self, folder_path: str):
        file_name = 'tickets.docx'
        file_path = os.path.join(folder_path, file_name)
        generator = Generator(self.theory_tasks, self.practice_tasks, self.ticket_amount,
                              self.theory_count, self.practice_count, self.include_none_complexity)
        tickets = generator.generate()
        generate_docx(file_path, tickets)
