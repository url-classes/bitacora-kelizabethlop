from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget
from playlist import Playlist
from os import path
import requests
from track import Track
from playlist_widget import PlayListWidget


def get_playlist(token: str, user_id: str) -> Playlist:
    user_headers = {
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/json'
    }
    playlist_id: str
    name: str
    description: str
    tracks: list[Track] = []

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
        items = get_playlist_response['tracks']['items']

        for item in items:
            track_name = item['track']['name']
            duration = item['track']['duration_ms']
            artists = []
            album = item['track']['album']
            album_cover = album['images'][0]['url']
            track = Track(track_name, duration, artists, album_cover)
            track.append(track)

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

    playlist = Playlist(playlist_id, name, description, tracks)
    return playlist


class PlaylistWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mi Playlist')
        self.layout = QVBoxLayout()

        self.title = QLabel()
        self.layout.addWidget(self.title)

        self.description = QLabel()
        self.layout.addWidget(self.description)

        label = QLabel('Listado de canciones:')
        self.layout.addWidget(label)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)

        self.setCentralWidget(self.main_widget)

    def load_ui(self, token: str, user_id: str):
        playlist = get_playlist(token, user_id)
        self.title.setText(playlist.name)
        self.description.setText(playlist.description)

        playlist_widget = PlayListWidget(playlist.tracks)
        self.layout.addWidget(playlist_widget)

        self.show()
