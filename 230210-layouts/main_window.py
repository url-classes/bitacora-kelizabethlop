from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QStackedLayout
from color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self). __init__()
        self.setWindowTitle('Layouts')

        layout = QVBoxLayout()
        layout.addWidget(ColorWidget('red'))
        layout.addWidget(ColorWidget('brown'))
        layout.addWidget(ColorWidget('black'))
        layout.addWidget(ColorWidget('sky blue'))
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        self.setWindowTitle('Layouts')

        layout = QHBoxLayout()
        layout.addWidget(ColorWidget('gray'))
        layout.addWidget(ColorWidget('violet'))
        layout.addWidget(ColorWidget('chocolate'))
        layout.addWidget(ColorWidget('light green'))
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()

        self.setWindowTitle('Layouts')

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(ColorWidget('red'))
        layout2.addWidget(ColorWidget('yellow'))
        layout2.addWidget(ColorWidget('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(ColorWidget('green'))

        layout3.addWidget(ColorWidget('red'))
        layout3.addWidget(ColorWidget('purple'))

        layout1.addLayout(layout3)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


class MainWindow4(QMainWindow):
    def __init__(self):
        super(MainWindow4, self).__init__()

        self.setWindowTitle('Layouts')

        layout = QGridLayout()

        layout.addWidget(ColorWidget('turquoise'), 0, 3)
        layout.addWidget(ColorWidget('light green'), 1, 1)
        layout.addWidget(ColorWidget('light blue'), 2, 2)
        layout.addWidget(ColorWidget('dark blue'), 3, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow5(QMainWindow):
    def __init__(self):
        super(MainWindow5, self).__init__()

        self.setWindowTitle('Layouts')

        layout = QStackedLayout()

        layout.addWidget(ColorWidget("red"))
        layout.addWidget(ColorWidget("green"))
        layout.addWidget(ColorWidget("blue"))
        layout.addWidget(ColorWidget("yellow"))

        layout.setCurrentIndex(1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
