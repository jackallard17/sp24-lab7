# [buffer]
from typing import Any


class BetterIterator:
    def __init__(self, text):
        self._text = text[:]

    def __iter__(self):
        return BetterCursor(self._text)
# [/buffer]

# [cursor]
class BetterCursor:
    def __init__(self, text):
        self._text = text
        self._row = 0
        self._col = -1

    def __next__(self):
        self._advance()
        if self._row == len(self._text):
            raise StopIteration
        return self._text[self._row][self._col]

    # [advance]
    def _advance(self):
        if self._row < len(self._text):
            self._col += 1
            if self._col == len(self._text[self._row]):
                self._row += 1
                self._col = 0
    # [/advance]
# [/cursor]

class ContextManager(BetterIterator):
    def __init__(self, func=None, value=None):
        super().__init__(func, value)
        self.original = None

    def __enter__(self):
        assert Exception is not None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        globals()[self.name] = self.original