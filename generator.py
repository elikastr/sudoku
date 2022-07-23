from solver import Solver
from random import choice

class Generator(Solver):
    def __init__(self):
        board = [[0] * 9 for _ in range(9)]
        Solver.__init__(self, board)

        self.backtrack(random=True)    # randomly fill the board using the backtracking algorithm form Solver
        self.__filled = [(r, c) for c in range(9) for r in range(9)]    # indices of filled cells

        self.solved_board = list(self.board)
        self.__remove()

    
    # remove random cells to generate a puzzle
    def __remove(self, n=5):
        while n > 0:
            r, c = choice(self.__filled)
            temp = self.board[r][c]
            self.board[r][c] = 0
            self.__filled.remove((r, c))

            if Solver(self.board).num_solutions() != 1:
                self.board[r][c] = temp
                self.__filled.append((r, c))
                n -= 1