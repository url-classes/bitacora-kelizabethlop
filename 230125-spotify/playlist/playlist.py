from track import Track


class Playlist:
    def __init__(self, playlist_id: str, name: str, description: str, tracks: list[Track]):
        self.id = playlist_id
        self.name = name
        self.description = description
        self.tracks = tracks
