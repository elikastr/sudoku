import collections
from random import shuffle

class Solver(object):
    def __init__(self, board):
        self.board = board
        self.solutions = 0
        self.rows = collections.defaultdict(set)     # rows[i] == list of filled digits in row i
        self.cols = collections.defaultdict(set)     # cols[i] == list of all filled digits in col i
        self.squares = collections.defaultdict(set)  # square[r // 3, c // 3] == list of all filled digits in the square
        self.empty = []                              # indices of empty cells

        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num == 0:
                    self.empty.append((r, c))
                else:
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.squares[r // 3, c // 3].add(num)

    
    # check if number n is valid in position [r, c]
    def valid(self, r, c, n):
        return not (n in self.rows[r] or
                    n in self.cols[c] or
                    n in self.squares[r // 3, c // 3])


    # find solution using backtracking algorithm
    # if solve == True, find 1 solution and fill board
    # if solve == False, find every possible solution - 
    #                    board reverts to starting state
    # if random == True, try to fill with numbers in a random order
    def backtrack(self, solve=True, random=False):
        if len(self.empty) == 0: 
            self.solutions += 1
            return True

        r, c = self.empty[-1]

        nums = [1,2,3,4,5,6,7,8,9]
        if random: shuffle(nums)
        for n in nums:
            if not self.valid(r, c, n): continue
            
            self.board[r][c] = n
            self.rows[r].add(n)
            self.cols[c].add(n)
            self.squares[r // 3, c // 3].add(n)
            self.empty.pop()

            if self.backtrack(solve, random) and solve: return True

            self.board[r][c] = 0
            self.rows[r].remove(n)
            self.cols[c].remove(n)
            self.squares[r // 3, c // 3].remove(n)
            self.empty.append((r, c))
        
        return False


    # find 1 solution and fill board
    def solve(self):
        return self.backtrack()


    # find number of all possible solutions without filling board
    def num_solutions(self):
        self.solutions = 0
        self.backtrack(solve=False)
        return self.solutions


    def print_board(self, board=None):
        s = ""

        rows = 0
        for r in range(9):
            rows += 1
            cols = 0
            for c in range(9):
                if board:
                    s += str(board[r][c]) + ' ' if board[r][c] else '  '
                else:
                    s += str(self.board[r][c]) + ' ' if self.board[r][c] else '  '
                cols += 1

                if cols % 3 == 0:
                    if cols == 9:
                        s += '\n'
                    else:
                        s += '| '
            if rows % 3 == 0 and rows != 9:
                s += '- - - - - - - - - - -\n'
        
        print(s)