import os


class File():
    def __init__(self, dirpath, name):
        self.path = os.path.join(dirpath, name)

    def get_body(self):
        return open(self.path, 'r').read().split("\n")
