import random
import math
from app.models.ticket import Ticket
from app.models.task import Task


class Generator:
    def __init__(self, theoretical_tasks: list[Task], practical_tasks: list[Task], num_tickets: int,
                 num_theoretical: int, num_practical: int,
                 initial_temp: int = 1000, alpha: int = 0.99, max_iterations: int = 1000,
                 include_none_complexity: bool = True):
        self.theoretical_tasks = theoretical_tasks
        self.practical_tasks = practical_tasks
        self.num_tickets = num_tickets
        self.num_theoretical = num_theoretical
        self.num_practical = num_practical
        self.initial_temp = initial_temp
        self.alpha = alpha
        self.max_iterations = max_iterations

        self._filter_tasks(include_none_complexity)

    def generate(self) -> list[Ticket]:
        tickets = []
        while len(tickets) < self.num_tickets:  # each time it generates only non overlapping tickets
            generated_tickets = self._simulated_annealing()
            if not generated_tickets:
                return tickets
            tickets += self._simulated_annealing()
        return tickets[:self.num_tickets]

    def _filter_tasks(self, include):
        if include:
            for index in range(len(self.theoretical_tasks)):
                if self.theoretical_tasks[index].complexity is None:
                    self.theoretical_tasks[index].complexity = 0
            for index in range(len(self.practical_tasks)):
                if self.practical_tasks[index].complexity is None:
                    self.practical_tasks[index].complexity = 0
        else:
            self.theoretical_tasks = [task for task in self.theoretical_tasks if task.complexity is not None]
            self.practical_tasks = [task for task in self.practical_tasks if task.complexity is not None]

    # noinspection PyMethodMayBeStatic
    def _swap_tasks(self, tasks) -> list[Task]:
        new_tasks = tasks.copy()
        idx1, idx2 = random.sample(range(len(tasks)), 2)
        new_tasks[idx1], new_tasks[idx2] = new_tasks[idx2], new_tasks[idx1]
        return new_tasks

    def _create_tickets(self, theoretical_tasks: list[Task], practical_tasks: list[Task]) -> list[Ticket]:
        tickets = []
        for i in range(self.num_tickets):
            start_theoretical = i * self.num_theoretical
            start_practical = i * self.num_practical
            theory = theoretical_tasks[start_theoretical:start_theoretical + self.num_theoretical]
            practice = practical_tasks[start_practical:start_practical + self.num_practical]
            # Ensuring each ticket has the required number of theoretical and practical tasks
            if len(theory) == self.num_theoretical and len(practice) == self.num_practical:
                tickets.append(Ticket(len(tickets), theory, practice))
        return tickets

    def _simulated_annealing(self) -> list[Ticket]:
        current_theoretical_tasks = random.sample(self.theoretical_tasks, len(self.theoretical_tasks))
        current_practical_tasks = random.sample(self.practical_tasks, len(self.practical_tasks))
        current_tickets = self._create_tickets(current_theoretical_tasks, current_practical_tasks)

        best_tickets = current_tickets
        best_stddev = stddev_complexity(current_tickets)

        temperature = self.initial_temp

        for _ in range(self.max_iterations):
            new_theoretical_tasks = self._swap_tasks(current_theoretical_tasks)
            new_practical_tasks = self._swap_tasks(current_practical_tasks)
            new_tickets = self._create_tickets(new_theoretical_tasks, new_practical_tasks)

            new_stddev = stddev_complexity(new_tickets)
            delta_stddev = new_stddev - stddev_complexity(current_tickets)

            if delta_stddev < 0 or random.random() < math.exp(-delta_stddev / temperature):
                current_theoretical_tasks = new_theoretical_tasks
                current_practical_tasks = new_practical_tasks
                current_tickets = new_tickets

                if new_stddev < best_stddev:
                    best_tickets = new_tickets
                    best_stddev = new_stddev

            temperature *= self.alpha

        return best_tickets


def mean_complexity(tickets: list[Ticket]):
    return sum(ticket.complexity() for ticket in tickets) / len(tickets)


def stddev_complexity(tickets: list[Ticket]):
    mean = mean_complexity(tickets)
    return (sum((ticket.complexity() - mean) ** 2 for ticket in tickets) / len(tickets)) ** 0.5
