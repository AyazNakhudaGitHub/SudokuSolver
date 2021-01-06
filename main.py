# Ayaz Nakhuda
import sys, pygame as pg
import time
from SudokuSolver import solve, check

pg.init()
screenSize = 750,750
screen = pg.display.set_mode(screenSize)
font = pg.font.SysFont(None,80)



sudokuBoard = [
    [0, 9, 1, 2, 0, 0, 8, 3, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 2, 0, 0, 0, 9, 0, 4, 7],
    [0, 5, 0, 0, 0, 3, 0, 8, 0],
    [6, 0, 0, 4, 1, 0, 0, 0, 0],
    [1, 0, 0, 8, 0, 0, 0, 9, 5],
    [0, 6, 0, 9, 0, 0, 0, 2, 0],
    [0, 0, 2, 3, 0, 0, 0, 0, 4],
    [8, 3, 0, 0, 4, 0, 1, 6, 0]
]

def drawBackground():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80 ) < 720:
        if (i % 3 > 0):
            lineWidth = 5
        else:
            lineWidth = 10

        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80) +15, 15), pg.Vector2((i *80)+15,735), lineWidth)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15,(i * 80) + 15), pg.Vector2(735, (i * 80) + 15), lineWidth)
        i+=1

def drawNumbers(board):
    offset = 39
    offset2 = 36
    for row in range(9):
        for col in range(9):
            output = board[row][col]
            if output == 0:
                output = " "
            text = font.render(str(output), True, pg.Color("black"))
            screen.blit(text, pg.Vector2((col *80) + offset, (row * 80) + offset2))

def gameLoop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    drawBackground()
    drawNumbers(sudokuBoard)
    pg.display.flip()
    time.sleep(10)
    callSolve(sudokuBoard)
    pg.display.flip()


def callSolve(sudokuBoard):
    solve(sudokuBoard)
    drawNumbers(sudokuBoard)


while 1:
    gameLoop()


