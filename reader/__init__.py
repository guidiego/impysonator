import os.path

from .recursive import recursive_read
from .file import File

def read(path):
    if not os.path.isfile(path):
        return recursive_read(path)
    else:
        return [File('', path)]