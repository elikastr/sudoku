import collections
from solver import Solver

class Generator(Solver):
    def __init__(self):
        board = [[0] * 9] * 9
        Solver.__init__(self, board)
