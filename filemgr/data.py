from typing import Optional
from os import listdir


class MyData:
    def __init__(self, root_path: Optional[str] = None):
        self._root = 'MyData/' if root_path is None else root_path

        self._streaming_history = self._load_streaming_history()
        self._playlists = self._load_playlists()
        self._user = None
        self._library = _MyLibrary(
                *self._load_my_library()
        )

    @property
    def streaming_history(self):
        return self._streaming_history

    @property
    def playlists(self):
        return self._playlists

    @property
    def user(self):
        raise NotImplementedError('Todo')

    @property
    def my_library(self):
        return self._library

    # data loaders (from file)
    def _load_streaming_history(self):
        files = list(filter(lambda x: x.startswith('StreamingHistory'), listdir(self._root)))
        files.sort()

        all_ = []
        for file in files:
            with open(self._root + file, encoding='UTF-8') as f:
                all_ += eval(f.read())

        return all_

    def _load_playlists(self):
        files = list(filter(lambda x: x.startswith('Playlist'), listdir(self._root)))
        files.sort()

        all_ = []
        for file in files:
            with open(self._root + file, encoding='UTF-8') as f:
                all_ += eval(f.read().replace('null', 'None'))['playlists']

        return all_

    def _load_my_library(self):
        with open(self._root + 'YourLibrary.json', encoding='UTF-8') as f:
            all_ = eval(f.read())

        return all_['tracks'], all_['albums'], all_['shows'], all_['episodes'], all_['artists']


class _MyLibrary:
    def __init__(self, songs, albums, shows, episodes, artists):
        self.liked_songs = songs
        self.liked_albums = albums
        self.liked_shows = shows
        self.liked_episodes = episodes
        self.following_artists = artists
