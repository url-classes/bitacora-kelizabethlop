from PyQt6.QtWidgets import QLabel, QMainWindow


class PlaylistWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel('Playlist Window')
        self.setCentralWidget(label)
