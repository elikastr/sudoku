import pygame as pg
from copy import deepcopy
from generator import Generator

pg.init()
size = 615, 615
diff = 65

screen = pg.display.set_mode(size)
font = pg.font.SysFont('arial', 35)

black = pg.Color('black')
blue = pg.Color('blue')
white = pg.Color('white')

gen = Generator()
board = deepcopy(gen.board)


def draw_grid():
    screen.fill(white)

    # draw the numbers
    for r in range(9):
        for c in range(9):
            if board[r][c]:
                if gen.board[r][c]: color = black
                else: color = blue

                text = font.render(str(board[r][c]), True, color)
                screen.blit(text, (r * diff + 40, c * diff + 30))

    # draw the lines
    for i in range(10):
        width = 1 if i % 3 else 4
        pg.draw.line(screen, black, (i * diff + 15, 15), (i * diff + 15, 600), width)
        pg.draw.line(screen, black, (15, i * diff + 15), (600, i * diff + 15), width)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            pass
    
    draw_grid()
    pg.display.update() 
