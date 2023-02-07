
import copy

from dlgo.gotypes import Player


class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert point is not None or is_pass or is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)


class GoString():
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)

    def merged_with(self, go_string):
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        combined_liberties = self.liberties | go_string.liberties - combined_stones
        return GoString(self.color, combined_stones, combined_liberties)

    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other) -> bool:
        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties
