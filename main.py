import sys
from PyQt6.QtWidgets import QApplication
from app.views.ticket_generator_view import TicketGeneratorView
from app.viewmodels.ticket_generator_viewmodel import TicketGeneratorViewModel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewmodel = TicketGeneratorViewModel()
    content_view = TicketGeneratorView(viewmodel)
    content_view.show()
    sys.exit(app.exec())
