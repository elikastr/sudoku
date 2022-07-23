import collections
from random import shuffle

class Solver(object):
    def __init__(self, board):
        self.board = board
        self.solutions = 0
        self.__rows = collections.defaultdict(set)     # rows[i] == list of filled digits in row i
        self.__cols = collections.defaultdict(set)     # cols[i] == list of all filled digits in col i
        self.__squares = collections.defaultdict(set)  # square[r // 3, c // 3] == list of all filled digits in the square
        self.__empty = []                              # indices of empty cells

        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num == 0:
                    self.__empty.append((r, c))
                else:
                    self.__rows[r].add(num)
                    self.__cols[c].add(num)
                    self.__squares[r // 3, c // 3].add(num)


    # find solution using backtracking algorithm
    # if solve == True, find 1 solution and fill board
    # if solve == False, find every possible solution - 
    #                    board reverts to starting state
    # if random == True, try to fill with numbers in a random order
    def __backtrack(self, solve=True, random=False):
        if len(self.__empty) == 0: 
            self.solutions += 1
            return True

        r, c = self.__empty[-1]

        nums = [1,2,3,4,5,6,7,8,9]
        if random: shuffle(nums)
        for n in nums:
            if (n in self.__rows[r] or
                n in self.__cols[c] or
                n in self.__squares[r // 3, c // 3]): continue
            
            self.board[r][c] = n
            self.__rows[r].add(n)
            self.__cols[c].add(n)
            self.__squares[r // 3, c // 3].add(n)
            self.__empty.pop()

            if self.__backtrack(solve, random) and solve: return True

            self.board[r][c] = 0
            self.__rows[r].remove(n)
            self.__cols[c].remove(n)
            self.__squares[r // 3, c // 3].remove(n)
            self.__empty.append((r, c))
        
        return False


    def solve(self):
        return self.__backtrack()


    def num_solutions(self):
        self.__backtrack(solve=False)
        return self.solutions


    def print_board(self):
        s = ""

        rows = 0
        for r in range(9):
            rows += 1
            cols = 0
            for c in range(9):
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


# def main():
#     board = [[5,3,0,0,7,0,0,0,0]
#             ,[6,0,0,1,9,5,0,0,0]
#             ,[0,9,8,0,0,0,0,6,0]
#             ,[8,0,0,0,6,0,0,0,3]
#             ,[4,0,0,8,0,3,0,0,1]
#             ,[7,0,0,0,2,0,0,0,6]
#             ,[0,6,0,0,0,0,2,8,0]
#             ,[0,0,0,4,1,9,0,0,5]
#             ,[0,0,0,0,8,0,0,7,9]]
    
#     solver = Solver(board)
#     # solver.print_board()
#     solver.solve()
#     solver.print_board()
#     # print(solver.solutions)


# if __name__ == '__main__':
#     main()