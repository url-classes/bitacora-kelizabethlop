from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel
from track import Track


class TrackWidget(QWidget):
    def __init__(self, track):
        super().__init__()

        self.setWindowTitle('TRACKS')
        layout1 = QHBoxLayout()

        self.image = QLabel()
        layout1.addWidget(self.image)

        layout2 = QVBoxLayout()
        self.title = QLabel(track.name)
        self.duration = QLabel(str(track.duration))
        layout2.addWidget(self.title)
        layout2.addWidget(self.duration)

        info_widget = QWidget()
        info_widget.setLayout(layout2)

        layout1.addWidget(info_widget)

        self.setLayout(layout1)
