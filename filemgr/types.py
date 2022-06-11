from time import struct_time
from datetime import timedelta
from typing import Optional, TypedDict


class Track(TypedDict):
    trackName: str
    artistName: str
    albumName: str
    trackUri: str  # spotify:track:<trackID>


class Item(TypedDict):
    track: Track
    episode: Optional[str]
    localTrack: Optional[str]
    addedDate: struct_time  # str  # yyyy-mm-dd


class PlayList(TypedDict):
    name: str
    lastModifiedDate: struct_time  # str  # yyyy-mm-dd
    items: list[Item]
    description: Optional[str]
    numberOfFollowers: int


class History(TypedDict):
    endTime: struct_time  # str  # yyyy-mm-dd HH:MM
    artistName: str
    trackName: str
    msPlayed: timedelta  # int
