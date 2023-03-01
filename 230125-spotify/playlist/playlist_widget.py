from PyQt6.QtWidgets import QVBoxLayout, QWidget
from track import Track
from track_widget import TrackWidget


class PlaylistWidget(QWidget):
    def __init__(self, tracks: list[Track]):
        super().__init__()
        layout = QVBoxLayout()

        for track in tracks:
            widget = TrackWidget(track)
            layout.addWidget(widget)

        self.setLayout(layout)
