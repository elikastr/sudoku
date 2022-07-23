import collections

class Solver(object):
    def __init__(self, board):
        self.board = board
        self.solutions = 0
        self.__rows = collections.defaultdict(set)
        self.__cols = collections.defaultdict(set)
        self.__squares = collections.defaultdict(set)
        self.__empty = []

        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num == 0:
                    self.__empty.append((r, c))
                else:
                    self.__rows[r].add(num)
                    self.__cols[c].add(num)
                    self.__squares[r // 3, c // 3].add(num)

    def __backtrack(self, solve=True):
        if len(self.__empty) == 0: 
            self.solutions += 1
            return True

        r, c = self.__empty[-1]

        for num in range(1, 10):
            if (num in self.__rows[r] or
                num in self.__cols[c] or
                num in self.__squares[r // 3, c // 3]): continue
            
            self.board[r][c] = num
            self.__rows[r].add(num)
            self.__cols[c].add(num)
            self.__squares[r // 3, c // 3].add(num)
            self.__empty.pop()

            if self.__backtrack(solve) and solve: return True

            self.board[r][c] = 0
            self.__rows[r].remove(num)
            self.__cols[c].remove(num)
            self.__squares[r // 3, c // 3].remove(num)
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