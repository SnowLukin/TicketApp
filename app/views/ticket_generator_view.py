from PyQt6.QtCore import Qt, QFile, QTextStream
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QCheckBox, QFileDialog, QSpinBox
from app.viewmodels.ticket_generator_viewmodel import TicketGeneratorViewModel


class TicketGeneratorView(QWidget):
    def __init__(self, viewmodel: TicketGeneratorViewModel):
        super().__init__()

        # Params
        self.viewmodel = viewmodel

        # Create widgets
        self.title_label = QLabel('TicketFusion', self)
        self.title_label.setObjectName('app_title')

        self.select_theory_label = QLabel('Theory File:', self)
        self.select_theory_button = QPushButton('Choose File', self)
        self.select_theory_button.setObjectName('select_button')

        self.select_practice_label = QLabel('Practice File:', self)
        self.select_practice_button = QPushButton('Choose File', self)
        self.select_practice_button.setObjectName('select_button')

        self.found_theory_tasks_label = QLabel(f'{len(self.viewmodel.theory_tasks)}', self)
        self.found_practice_tasks_label = QLabel(f'{len(self.viewmodel.practice_tasks)}', self)

        self.ticket_amount_label = QLabel('Number of exams tickets to generate:', self)
        self.ticket_amount_input = QSpinBox(self)
        self.ticket_amount_input.setFixedWidth(40)
        self.ticket_amount_input.setRange(1, 99)

        self.theory_count_label = QLabel('Number of theory tasks per ticket:', self)
        self.practice_count_label = QLabel('Number of practice tasks per ticket:', self)
        self.theory_count_input = QSpinBox(self)
        self.theory_count_input.setFixedWidth(40)
        self.theory_count_input.setRange(0, 10)
        self.practice_count_input = QSpinBox(self)
        self.practice_count_input.setFixedWidth(40)
        self.practice_count_input.setRange(0, 10)

        self.include_none_checkbox = QCheckBox('Include tasks with no complexity', self)
        self.generate_tickets_button = QPushButton('Generate Exam Tickets', self)
        self.generate_tickets_button.setFixedSize(180, 45)
        self.generate_tickets_button.setObjectName('generate_button')

        self.dev_label = QLabel('Developed by Snow Lukin', self)
        self.dev_label.setObjectName('dev_label')

        # Create layouts
        self.layout = QVBoxLayout()
        self.layout.setSpacing(22)
        self.layout.addWidget(self.title_label)
        self.layout.setAlignment(self.title_label, Qt.AlignmentFlag.AlignCenter)

        self.theory_layout = QHBoxLayout()
        self.theory_layout.addWidget(self.select_theory_label)
        self.theory_layout.addWidget(self.select_theory_button)
        self.theory_layout.addWidget(self.found_theory_tasks_label)

        self.practice_layout = QHBoxLayout()
        self.practice_layout.addWidget(self.select_practice_label)
        self.practice_layout.addWidget(self.select_practice_button)
        self.practice_layout.addWidget(self.found_practice_tasks_label)

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

        self.layout.addLayout(self.ticket_amount_layout)
        self.layout.addLayout(self.min_complexity_layout)
        self.layout.addLayout(self.max_complexity_layout)

        self.layout.addWidget(self.include_none_checkbox)
        self.layout.setAlignment(self.include_none_checkbox, Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.generate_tickets_button)
        self.layout.setAlignment(self.generate_tickets_button, Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.dev_label)
        self.layout.setAlignment(self.dev_label, Qt.AlignmentFlag.AlignTrailing)

        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the widget
        self.setLayout(self.layout)
        self.setFixedSize(416, 430)
        self.load_stylesheet()

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
            self.found_theory_tasks_label.setText(f'{len(self.viewmodel.theory_tasks)}')
            self.select_theory_button.setText(file_name.split('/')[-1])

    def select_practice_file(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open .docx File", "",
                                                   "Word Documents (*.docx);;All Files (*)", options=options)
        if file_name:
            self.viewmodel.select_practice_file(file_name)
            self.found_practice_tasks_label.setText(f'{len(self.viewmodel.practice_tasks)}')
            self.select_practice_button.setText(file_name.split('/')[-1])

    def generate_tickets(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder to Save .docx File", "")
        if folder_path:
            self.viewmodel.ticket_amount = int(self.ticket_amount_input.text())
            self.viewmodel.theory_count = int(self.theory_count_input.text())
            self.viewmodel.practice_count = int(self.practice_count_input.text())
            self.viewmodel.include_none_complexity = self.include_none_checkbox.isChecked()
            self.viewmodel.generate_tickets(folder_path)

    def load_stylesheet(self):
        style_file = QFile("app/views/ticket_generator_view_styles.qss")
        style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
        stream = QTextStream(style_file)
        stylesheet = stream.readAll()
        self.setStyleSheet(stylesheet)
