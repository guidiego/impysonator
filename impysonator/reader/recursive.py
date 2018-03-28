import os

from .file import File

def recursive_read(topdir):
    results = []
    topdir = os.path.join(os.getcwd(), *topdir.split("/"))

    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            f = File(dirpath, name)
            results.append(f)

    return results