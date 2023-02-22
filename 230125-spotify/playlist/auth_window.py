from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        login_button = QPushButton('Ingresar')
        login_button.cliked.connect(self.open_browser)

        refresh_button = QPushButton('Volver a intentar')
        refresh_button.clicked.connect(self.try_again)

        layout = QVBoxLayout()
        layout.addWidget(login_button)
        layout.addWidget(refresh_button)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

