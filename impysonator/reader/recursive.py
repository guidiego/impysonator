import os

from .file import File

def recursive_read(topdir):
    results = []

    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            f = File(dirpath, name)
            results.append(f)

    return results