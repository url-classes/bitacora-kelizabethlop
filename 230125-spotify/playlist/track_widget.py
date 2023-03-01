from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QImage, QPixmap
from track import Track
import requests


class TrackWidget(QWidget):
    def __init__(self, track: Track):
        super().__init__()
        layout1 = QHBoxLayout()
        image_data = requests.get(track.album_cover).content
        pixmap = QImage()
        pixmap.loadFromData(image_data)

        self.image = QLabel()
        self.image.setPixmap(QPixmap(pixmap))
        self.image.setFixedHeight(128)
        self.image.setFixedWidth(128)
        self.image.setScaledContents(True)
        layout1.addWidget(self.image)

        layout2 = QVBoxLayout()
        self.title = QLabel(track.name)
        self.duration = QLabel(track.duration_min)
        layout2.addWidget(self.title)
        layout2.addWidget(self.duration)

        info_widget = QWidget()
        info_widget.setLayout(layout2)

        layout1.addWidget(info_widget)

        self.setLayout(layout1)
