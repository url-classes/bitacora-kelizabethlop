from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon,  QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python QLabel")
        self.setWindowIcon(QIcon('EE6FRKIE2FHZVD3ZOLQY6CAL54.avif'))

        label = QLabel(self)
        pixmap = QPixmap('EE6FRKIE2FHZVD3ZOLQY6CAL54.avif')
        label.setPixmap(pixmap)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
