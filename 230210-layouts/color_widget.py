from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor


class ColorWidget(QWidget):
    def __init__(self, color: str):
        super(ColorWidget, self). __init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))

        self.setPalette(palette)
