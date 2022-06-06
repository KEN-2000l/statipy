from typing import Optional
from zipfile import ZipFile
import os

from .data import MyData


def _extract_data(path: str):
    if not os.path.exists('MyData'):
        with ZipFile(path) as zip_:
            zip_.extractall()


def load_zipped_data(path: Optional[str] = None):
    if path is None:
        path = 'my_spotify_data.zip'
    _extract_data(path)

    return MyData()
