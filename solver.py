import collections

class Solver(object):
    def __init__(self, board):
        self.board = board
        self.rows = collections.defaultdict(set)
        self.cols = collections.defaultdict(set)
        self.squares = collections.defaultdict(set)
        self.empty = []

    def backtrack(self):
        if len(self.empty) == 0: 
            return True

        r, c = self.empty[-1]

        for num in range(1, 10):
            if (num in self.rows[r] or
                num in self.cols[c] or
                num in self.squares[r // 3, c // 3]): continue
            
            self.board[r][c] = num
            self.rows[r].add(num)
            self.cols[c].add(num)
            self.squares[r // 3, c // 3].add(num)
            self.empty.pop()

            if self.backtrack(): return True

            self.board[r][c] = 0
            self.rows[r].remove(num)
            self.cols[c].remove(num)
            self.squares[r // 3, c // 3].remove(num)
            self.empty.append((r, c))
        
        return False

    def solve(self):
        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num == 0:
                    self.empty.append((r, c))
                else:
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.squares[r // 3, c // 3].add(num)

        return self.backtrack()
    
    def print_board(self):
        s = ""

        r_count = 0
        for r in range(9):
            r_count += 1
            c_count = 0
            for c in range(9):
                s += str(self.board[r][c]) + ' ' if self.board[r][c] else '  '
                c_count += 1

                if c_count % 3 == 0:
                    if c_count == 9:
                        s += '\n'
                    else:
                        s += '| '
            if r_count % 3 == 0 and r_count != 9:
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
#     solver.print_board()
#     solver.solve()
#     solver.print_board()


# if __name__ == '__main__':
#     main()