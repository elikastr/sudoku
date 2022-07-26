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

gen = Generator()


class Cell(object):
    def __init__(self, r, c):
        self.rect = pg.Rect((15 + r * diff, 15 + c * diff), (diff, diff))
        self.val = gen.board[r][c]
        self.default = True if self.val else False

    def draw(self, selected=False):
        width = 5 if selected else 1
        line_color = red if selected else black

        pg.draw.rect(screen, line_color, self.rect, width)

        # draw number
        if self.val == 0: return
        
        text = font.render(str(self.val), True, black if self.default else blue)
        screen.blit(text, (self.rect.x + 25, self.rect.y + 15))

    def update_val(self, val):
        if self.default: return
        self.val = val


class Board(object):
    def __init__(self):
        self.cells = []
        for r in range(9):
            row = []
            for c in range(9):
                cell = Cell(r, c)
                row.append(cell)
            self.cells.append(row)

        self.selected = None

    def draw(self):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].draw()
        if self.selected:
            r, c = self.selected
            self.cells[r][c].draw(True)


board = Board()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            # update selected cell
            pos = pg.mouse.get_pos()
            x, y = pos[0] // diff, pos[1] // diff
            if 0 <= x < 9 and 0 <= y < 9:
                board.selected = x, y
    
    # drawing the grid
    screen.fill(white)

    # draw the bold lines 
    for i in range(0, 10, 3):
        pg.draw.line(screen, black, (i * diff + 15, 15), (i * diff + 15, 600), 4)
        pg.draw.line(screen, black, (15, i * diff + 15), (600, i * diff + 15), 4)

    # draw the grid
    board.draw()

    pg.display.update() 
