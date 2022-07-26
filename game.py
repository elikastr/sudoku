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
        self.r, self.c = r, c
        self.val = gen.board[r][c]

        if self.val: self.text_color = black
        else: self.text_color = blue

    def draw(self, selected=False):
        x, y = 15 + self.r * diff, 15 + self.c * diff

        # draw lines
        width = 5 if selected else 1
        line_color = red if selected else black

        pg.draw.line(screen, line_color, (x, y), (x + diff, y), width)
        pg.draw.line(screen, line_color, (x, y + diff), (x + diff, y + diff), width)
        pg.draw.line(screen, line_color, (x, y), (x, y + diff), width)
        pg.draw.line(screen, line_color, (x + diff, y), (x + diff, y + diff), width)

        # draw number
        if self.val == 0: return
        
        text = font.render(str(self.val), True, self.text_color)
        screen.blit(text, (x + 25, y + 15))


class Board(object):
    def __init__(self):
        self.nums = []
        for r in range(9):
            row = []
            for c in range(9):
                cell = Cell(r, c)
                row.append(cell)
            self.nums.append(row)

        self.selected = None

    def draw(self):
        for r in range(9):
            for c in range(9):
                self.nums[r][c].draw()
        if self.selected:
            r, c = self.selected
            self.nums[r][c].draw(True)


board = Board()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
            # TODO: update selected cell
    
    # drawing the grid
    screen.fill(white)

    # draw the bold lines 
    for i in range(0, 10, 3):
        pg.draw.line(screen, black, (i * diff + 15, 15), (i * diff + 15, 600), 4)
        pg.draw.line(screen, black, (15, i * diff + 15), (600, i * diff + 15), 4)

    # draw the grid
    board.draw()

    pg.display.update() 
