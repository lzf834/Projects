import time

board = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0]
]

def puzzlePrinter(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("-+-+-+-+-+-+-+-+-+-+-+-")
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end = "")

def findEmpty(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 0:
                return (x, y)
    return None

def isValid(puzzle, row, col, value):
    #check row and col within board
    if row < 0 or row > 8 or col < 0 or col > 8:
        return False

    #check in row
    for i in puzzle[row]:
        if value == i:
            return False

    #check in column
    for rows in puzzle:
        if rows[col] == value:
            return False

    #check in minigrid
    minigridRow = row // 3 * 3
    minigridCol = col // 3 * 3

    for x in range(minigridRow, minigridRow + 2):
        for y in range(minigridCol, minigridCol + 2):
            if puzzle[x][y] == value:
                return False

    return True

#TWT solution - recursive solution
def solve(puzzle):
    coords = findEmpty(puzzle)

    if coords == None:
        return True
    else:
        row = coords[0]
        col = coords[1]

        for number in range(1, 10):
            if isValid(puzzle, row, col, number):
                puzzle[row][col] = number
                # solve(puzzle)

                if solve(puzzle):
                    return True

                puzzle[row][col] = 0

        return False

# def solve(puzzle):
#     history = []
#     isSolved = False
#     x = 1

#     while not isSolved:
#         coords = findEmpty(puzzle)

#         if coords == None:
#             isSolved = True
        
#         else:
#             row = coords[0]
#             col = coords[1]

#             for number in range(x, 10):
#                 if isValid(puzzle, row, col, number):
#                     puzzle[row][col] = number
#                     history.append([row, col, number])
#                     x = 1
            
#             prev = history.pop()
#             x = prev[2]
#             puzzle[prev[0]][prev[1]] = 0

puzzlePrinter(board)
#start timer
start = time.time()

solve(board)

#end timer
end = time.time()
print(end - start)

print("-------------------------------------")
puzzlePrinter(board)