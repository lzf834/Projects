import pygame
import copy
from main import isValid, findEmpty

# init font module
pygame.font.init()
# set screen size
screen = pygame.display.set_mode((500, 600))

# Title
pygame.display.set_caption("Sudoku")

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Test board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

base = copy.deepcopy(board)

# fonts to be used
textFont = pygame.font.SysFont("comicsans", 40)
instructionFont = pygame.font.SysFont("comicsans", 30)
numberFont = pygame.font.SysFont("harlowsolid", 40)

# values
x = 0
y = 0
dif = 500 / 9
val = 0

# function to get coords
def getCoord(xy):
    # global keyword allows variable to be accessed outside of its original scope
    global x
    global y

    x = xy[0]//dif
    y = xy[1]//dif


# Cell highlight
def highlightBox():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 

# draw sudoku grids
def draw(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:

                # if already numbered, fill green colour
                pygame.draw.rect(screen, (80, 220, 100), (i * dif, j * dif, dif + 1, dif + 1)) 

                # fill grids with defaults numbers provided

                # render(text, antialias, color, background)
                number = textFont.render(str(puzzle[i][j]), 1, (0, 0, 0))
                # blit(source, dest, area=None, special_flags=0)
                screen.blit(number, (i * dif + 15, j * dif + 15))

    # draw grids - horizontal and vertical lines
    for i in range(10):
        if i % 3 == 0:
            lineThickness = 7
        else:
            lineThickness = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), lineThickness)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), lineThickness)

# enter values into empty squares
def enterValue(val):
    number = numberFont.render(str(val), 1, (0, 0, 0))
    screen.blit(number, (x * dif + 15, y * dif + 15))

# Produce error for invalid entries
def prodError():
    errorText = textFont.render("Invalid Entry", 1, (0, 0, 0))
    screen.blit(errorText, (20, 570))

def solve(puzzle):
    coords = findEmpty(puzzle)

    pygame.event.pump()

    if coords == None:
        return True
    else:
        row = coords[0]
        col = coords[1]

        for number in range(1, 10):
            if isValid(puzzle, row, col, number):
                puzzle[row][col] = number

                global x, y
                x = row
                y = col

                # set white background
                screen.fill((255, 255, 255))

                # Draw out the setup
                draw(puzzle)
                highlightBox()
                
                pygame.display.update()
                pygame.time.delay(20)

                # solve(puzzle)
                if solve(puzzle):
                    return True

                puzzle[row][col] = 0

                screen.fill((255, 255, 255))
                draw(puzzle)
                highlightBox()
                pygame.display.update()
                pygame.time.delay(50)

        return False

# display instructions for game
def instruction():
    line1 = instructionFont.render("Press D to reset R to empty", 1, (0, 0, 0))
    line2 = instructionFont.render("Enter values and press Enter to key in", 1, (0, 0, 0))

    screen.blit(line1, (20, 520))
    screen.blit(line2, (20, 540))

# display options when sudoku has been solved
def result():
    finishLine = instructionFont.render("You have completed the puzzle, press R or D", 1, (0, 0, 0))
    screen.blit(finishLine, (20, 570))

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# run loop
while run:
    # set white BG
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            getCoord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2    
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6 
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9  
            if event.key == pygame.K_RETURN:
                flag2 = 1   
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                for i in range(9):
                    for j in range(9):
                        board[i][j] = 0

            # If D is pressed reset the board to default 
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                for i in range(9):
                    for j in range(9):
                        board[i][j] = base[i][j]

    if flag2 == 1:
        if not solve(board):
            error = 1
        else:
            rs = 1

        flag2 = 0
    
    if val != 0:
        enterValue(val)
        row = int(x)
        col = int(y)

        if isValid(board, row, col, val):
            board[row][col] = val
            flag1 = 0
        else:
            board[row][col] = 0
            prodError()
        val = 0

    if error == 1:
        prodError()
    if rs == 1:
        result()
    draw(board)

    if flag1 == 1:
        highlightBox()

    instruction()

    pygame.display.update()

pygame.quit()
