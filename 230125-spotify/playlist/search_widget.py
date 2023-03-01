from PyQt6.QtWidgets import QWidget, QVBoxLayout
from track import Track
from track_widget import TrackWidget


class SearchWidget(QWidget):
    def __init__(self, tracks: list[Track], search: str):
        super().__init__()
        layout = QVBoxLayout()
        for track in tracks:
            if search.lower() == track.name.lower():
                widget = TrackWidget(track)
                layout.addWidget(widget)
        self.setLayout(layout)
