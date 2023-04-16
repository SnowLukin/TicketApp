from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QCheckBox, QFileDialog
from app.viewmodels.ticket_generator_viewmodel import TicketGeneratorViewModel


class TicketGeneratorView(QWidget):
    def __init__(self, viewmodel: TicketGeneratorViewModel):
        super().__init__()

        # Params
        self.viewmodel = viewmodel

        # Create widgets
        self.select_theory_button = QPushButton('Файл Теория', self)
        self.select_practice_button = QPushButton('Файл Практика', self)

        self.found_theory_tasks_label = QLabel(
            f'Найдено теоретических заданий: {len(self.viewmodel.theory_tasks)}', self
        )
        self.found_practice_tasks_label = QLabel(
            f'Найдено практических заданий: {len(self.viewmodel.practice_tasks)}', self
        )

        self.ticket_amount_label = QLabel('Количество билетов:', self)
        self.ticket_amount_input = QLineEdit(self)

        self.theory_count_label = QLabel('Количество Теории:', self)
        self.practice_count_label = QLabel('Количество Практики:', self)
        self.theory_count_input = QLineEdit(self)
        self.practice_count_input = QLineEdit(self)

        self.include_none_checkbox = QCheckBox('Учитывать задания без сложности', self)
        self.generate_tickets_button = QPushButton('Получить Билеты', self)

        # Create layouts
        self.layout = QVBoxLayout()

        self.theory_layout = QHBoxLayout()
        self.theory_layout.addWidget(self.select_theory_button)

        self.practice_layout = QHBoxLayout()
        self.practice_layout.addWidget(self.select_practice_button)

        self.ticket_amount_layout = QHBoxLayout()
        self.ticket_amount_layout.addWidget(self.ticket_amount_label)
        self.ticket_amount_layout.addWidget(self.ticket_amount_input)

        self.min_complexity_layout = QHBoxLayout()
        self.min_complexity_layout.addWidget(self.theory_count_label)
        self.min_complexity_layout.addWidget(self.theory_count_input)

        self.max_complexity_layout = QHBoxLayout()
        self.max_complexity_layout.addWidget(self.practice_count_label)
        self.max_complexity_layout.addWidget(self.practice_count_input)

        # Add widgets to the layout
        self.layout.addLayout(self.theory_layout)
        self.layout.addLayout(self.practice_layout)
        self.layout.addWidget(self.found_theory_tasks_label)
        self.layout.addWidget(self.found_practice_tasks_label)
        self.layout.addLayout(self.ticket_amount_layout)
        self.layout.addLayout(self.min_complexity_layout)
        self.layout.addLayout(self.max_complexity_layout)
        self.layout.addWidget(self.include_none_checkbox)
        self.layout.addWidget(self.generate_tickets_button)

        # Set the layout for the widget
        self.setLayout(self.layout)

        # Connect signals to slots
        self.select_theory_button.clicked.connect(self.select_theory_file)
        self.select_practice_button.clicked.connect(self.select_practice_file)
        self.generate_tickets_button.clicked.connect(self.generate_tickets)

    def select_theory_file(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open .docx File", "",
                                                   "Word Documents (*.docx);;All Files (*)", options=options)
        if file_name:
            self.viewmodel.select_theory_file(file_name)
            self.found_theory_tasks_label.setText(f'Найдено теоретических заданий: {len(self.viewmodel.theory_tasks)}')

    def select_practice_file(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open .docx File", "",
                                                   "Word Documents (*.docx);;All Files (*)", options=options)
        if file_name:
            self.viewmodel.select_practice_file(file_name)
            self.found_practice_tasks_label.setText(
                f'Найдено практических заданий: {len(self.viewmodel.practice_tasks)}')

    def generate_tickets(self):
        # options = QFileDialog.Option.ReadOnly
        # file_name, _ = QFileDialog.getOpenFileName(self, "Save .docx File", "",
                                                   # "Word Documents (*.docx);;All Files (*)", options=options)
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder to Save .docx File", "")
        if folder_path:
            self.viewmodel.ticket_amount = int(self.ticket_amount_input.text())
            self.viewmodel.theory_count = int(self.theory_count_input.text())
            self.viewmodel.practice_count = int(self.practice_count_input.text())
            self.viewmodel.include_none_complexity = self.include_none_checkbox.isChecked()
            self.viewmodel.generate_tickets(folder_path)
