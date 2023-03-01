from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QApplication, QLineEdit
from playlist import Playlist
from os import path
import sys
import requests
from track import Track
from search_widget import SearchWidget


app = QApplication(sys.argv)


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
            track = Track(track_name, duration, album_cover, artists)
            tracks.append(track)

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


class SearchWindow(QMainWindow):
    def __init__(self, token: str, user_id: str):
        super().__init__()
        self.playlist = get_playlist(token, user_id)

        self.setWindowTitle('Mi Playlist')
        self.layout = QVBoxLayout()

        self.search_button = QPushButton('Search')
        self.new_search_button = QPushButton('New Search')

        self.title = QLabel()
        self.title.setText(self.playlist.name)
        self.layout.addWidget(self.title)

        self.description = QLabel()
        self.layout.addWidget(self.description)
        label = QLabel('Listado de canciones:')
        self.layout.addWidget(label)

        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.search_button.clicked.connect(self.busqueda)
        self.layout.addWidget(self.search_button)
        self.new_search_button.hide()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)

        self.setCentralWidget(self.main_widget)

    def busqueda(self):
        search = self.textbox.text()
        searchwindow = SearchWidget(self.playlist.tracks, search)
        self.layout.addWidget(searchwindow)
