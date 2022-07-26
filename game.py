import sys
import pygame as pg
from generator import Generator

pg.init()
size = 615, 615
diff = 65

screen = pg.display.set_mode(size)
font = pg.font.SysFont('arial', 35)

black = pg.Color('black')
blue = pg.Color('blue')
white = pg.Color('white')
red = pg.Color('red')
cyan = pg.Color('cyan')

gen = Generator()


class Cell(object):
    def __init__(self, r, c):
        self.rect = pg.Rect((15 + r * diff, 15 + c * diff), (diff, diff))
        self.val = gen.board[r][c]
        self.default = True if self.val else False

    def select(self):
        pg.draw.rect(screen, cyan, self.rect)

    def draw_number(self):
        if self.val == 0: return
        text = font.render(str(self.val), True, black if self.default else blue)
        screen.blit(text, (self.rect.x + 25, self.rect.y + 15))

    def update_val(self, val):
        if self.default: return
        self.val = val


board = []
for r in range(9):
    row = []
    for c in range(9):
        cell = Cell(r, c)
        row.append(cell)
    board.append(row)


def draw_numbers():
    for r in range(9):
        for c in range(9):
            board[r][c].draw_number()


screen.fill(white)   
draw_numbers()

while True:
    x, y = -1, -1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill(white)

            # select cell
            pos = pg.mouse.get_pos()
            x, y = pos[0] // diff, pos[1] // diff
            if 0 <= x < 9 and 0 <= y < 9:
                board[x][y].select()  

            draw_numbers()   

        # if event.type == pg.KEYDOWN and board.selected:
        #     # update selected cell
        #     x, y = board.selected
        #     if event.key == pg.K_BACKSPACE or event.key == pg.K_0:
        #         val = 0
        #     if event.key == pg.K_1:
        #         val = 1
        #     if event.key == pg.K_2:
        #         val = 2
        #     if event.key == pg.K_3:
        #         val = 3
        #     if event.key == pg.K_4:
        #         val = 4
        #     if event.key == pg.K_5:
        #         val = 5
        #     if event.key == pg.K_6:
        #         val = 6
        #     if event.key == pg.K_7:
        #         val = 7
        #     if event.key == pg.K_8:
        #         val = 8
        #     if event.key == pg.K_9:
        #         val = 9
        #     board.cells[x][y].update_val(val)

    # draw the grid
    for i in range(10):
        width = 1 if i % 3 else 4
        pg.draw.line(screen, black, (i * diff + 15, 15), (i * diff + 15, 600), width)
        pg.draw.line(screen, black, (15, i * diff + 15), (600, i * diff + 15), width)

    pg.display.update() 
