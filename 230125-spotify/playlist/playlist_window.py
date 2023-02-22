from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget
from playlist import Playlist
from os import path
import requests


def get_playlist(token: str, user_id: str) -> Playlist:
    user_headers = {
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/json'
    }
    playlist_id: str
    name: str
    description: str

    if path.isfile('../playlist.txt'):
        file = open('../playlist.txt', 'r')
        playlist_id = file.read()
        file.close()

        endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        get_playlist_response = requests.get(
            endpoint,
            headers=user_headers
        ).json()

        name = get_playlist_response['name']
        description = get_playlist_response['description']
    else:
        endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists'
        body = {
            "name": "Mi nueva playlist",
            "description": "Esta playlist es del curso de Estructura de Datos I"
        }

        create_playlist_response = requests.post(
            endpoint,
            json=body,
            headers=user_headers
        ).json()

        playlist_id = create_playlist_response['id']
        name = create_playlist_response['name']
        description = create_playlist_response['description']

        file = open('../playlist.txt', 'w')
        file.write(playlist_id)

    playlist = Playlist(playlist_id, name, description)
    return playlist


class PlaylistWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mi Playlist')
        layout = QVBoxLayout()

        self.title = QLabel()
        layout.addWidget(self.title)

        self.description = QLabel()
        layout.addWidget(self.description)

        label = QLabel('Listado de canciones:')
        layout.addWidget(label)

        self.main_widget = QWidget()
        self.main_widget.setLayout(layout)

        self.setCentralWidget(self.main_widget)

    def load_ui(self, token: str, user_id: str):
        playlist = get_playlist(token, user_id)
        self.title.setText(playlist.name)
        self.description.setText(playlist.description)

        self.show()
