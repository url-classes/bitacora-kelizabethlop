class Track:
    def __init__(self, name: str, duration: int, album_cover: str, artists: list[str]):
        self.name = name
        self.duration = duration
        self.album_cover = album_cover
        self.artists = artists

    def duration_min(self) -> str:
        duration_seconds = self.duration / 1000
        minutes = duration_seconds // 60
        seconds = duration_seconds - (minutes * 60) / 1000
        return f'{int(minutes)}:{int(seconds)}'
