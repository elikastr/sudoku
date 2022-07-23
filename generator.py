import collections
from random import randint, shuffle
from solver import Solver

class Generator(Solver):
    def __init__(self):
        board = [[0] * 9 for _ in range(9)]
        Solver.__init__(self, board)

        self.fill()
        self.__filled = [(r, c) for c in range(9) for r in range(9)]     # indices of filled cells


    def fill(self):
        self.backtrack(random=True)