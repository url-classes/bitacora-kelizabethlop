import sys

import requests
from PyQt6.QtGui import QPixmap,QImage
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel


app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Imagen de Internet")

        label = QLabel(self)
        url = 'https://www.hogarmania.com/archivos/201204/cerezo01-668x400x80xX.jpg'
        image = QImage()
        image.loadFromData(requests.get(url).content)

        pixmap = QPixmap(image)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)


w = MainWindow()
w.show()
sys.exit(app.exec())


