import collections

class Solver(object):
    def __init__(self, board):
        self.board = board

    def solve(self):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        empty = []

        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num == 0:
                    empty.append((r, c))
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[r // 3, c // 3].add(num)
        
        def backtrack():
            if len(empty) == 0: return True

            r, c = empty[-1]

            for num in range(1, 10):
                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[r // 3, c // 3]): continue
                
                self.board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                squares[r // 3, c // 3].add(num)
                empty.pop()

                if backtrack(): return True

                self.board[r][c] = 0
                rows[r].remove(num)
                cols[c].remove(num)
                squares[r // 3, c // 3].remove(num)
                empty.append((r, c))
            
            return False
        
        if not backtrack(): print("No solution\n")
        else: self.print_board()
    
    def print_board(self):
        s = ""

        r_count = 0
        for r in range(9):
            r_count += 1
            c_count = 0
            for c in range(9):
                s += str(self.board[r][c]) + ' '
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

# if __name__ == '__main__':
#     main()