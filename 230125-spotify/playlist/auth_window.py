import webbrowser

from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from communicate import Communicate


class AuthWindow(QMainWindow):
    def __init__(self, communicate: Communicate):
        super().__init__()

        self.setWindowTitle('Iniciar sesión')
        self.communicate = communicate

        login_button = QPushButton('Ingresar')
        login_button.clicked.connect(self.open_browser)

        refresh_button = QPushButton('Volver a intentar')
        refresh_button.clicked.connect(self.try_again)

        layout = QVBoxLayout()
        layout.addWidget(login_button)
        layout.addWidget(refresh_button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def open_browser(self):
        webbrowser.open('http://localhost:7777/authorize')

    def try_again(self):
        self.communicate.verify_code.emit()

