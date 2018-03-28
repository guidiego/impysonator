from .contants import IMPERSONAL_EXPRESSIONS

class Impersonal():
    def __init__(self, line, index):
        self._line = line
        self._index = index
        self.matches = []

        self._get_matches()

    def has_matches(self):
        return len(self.matches) > 0

    def _get_matches(self):
        for exp in IMPERSONAL_EXPRESSIONS:
            for m in exp.findall(self._line):
                self.matches.append({
                    "line": self._index,
                    "word": m
                })