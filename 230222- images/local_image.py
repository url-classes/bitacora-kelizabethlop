import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel


app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Imagen Local")

        label = QLabel(self)
        pixmap = QPixmap('cerezo.jpg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)


w = MainWindow()
w.show()
sys.exit(app.exec())


