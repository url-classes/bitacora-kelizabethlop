from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self). __init__()
        self.setWindowTitle('Layouts')

        layout = QVBoxLayout()
        layout.addWidget(ColorWidget('red'))
        layout.addWidget(ColorWidget('brown'))
        layout.addWidget(ColorWidget('black'))
        layout.addWidget(ColorWidget('skyblue'))
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        self.setWindowTitle('Layouts')

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(ColorWidget('red'))
        layout2.addWidget(ColorWidget('yellow'))
        layout2.addWidget(ColorWidget('purple'))
        layout1.addWidget(ColorWidget('green'))

        layout3.addWidget(ColorWidget('red'))
        layout3.addWidget(ColorWidget('purple'))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)