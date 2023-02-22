from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        login_button = QPushButton('Ingresar')
        refresh_button = QPushButton('Volver a intentar')

        layout = QVBoxLayout()
        layout.addWidget(login_button)
        layout.addWidget(refresh_button)

        widget = QWidget()
        widget.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setCentralWidget(widget)

