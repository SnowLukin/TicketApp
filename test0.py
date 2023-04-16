from app.models.ticket_generator import Generator
from app.models.task_utils import generate_tasks
from app.models.task import TaskType
from utils.docx_utils import generate_docx
from utils.docx_parser import extract_practice, extract_theory

theory_path = '/Users/snowlukin/Desktop/Нечеткая математика примеры/Perechen_Voprosov_Vo_-56_-_2021.docx'
practice_path = '/Users/snowlukin/Desktop/Нечеткая математика примеры/Perechen_Pz_Dlya_Podgotovki_Vo-56_2021.docx'

theory_text = extract_theory(theory_path)
practice_text = extract_practice(practice_path)

theory_tasks = generate_tasks(theory_text, TaskType.theory)
practice_tasks = generate_tasks(practice_text, TaskType.practice)

print('Amount of theory tasks: ', len(theory_tasks))
print('Amount of practice tasks: ', len(practice_tasks))

ticket_gen = Generator(theory_tasks, practice_tasks, 30, 4, 3, include_none_complexity=True)
tickets = ticket_gen.generate()

for i, ticket in enumerate(tickets, 1):
    print(f"Ticket {i} #{ticket.complexity()}:")
    print(' Theoretical complexity: ', ticket.theory_complexity())
    print(' Practical complexity: ', ticket.practice_complexity())

generate_docx('test.docx', tickets)
