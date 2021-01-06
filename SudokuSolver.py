# Ayaz Nakhuda

def solve(board):
    find = findEmpty(board)
    if not find:
        return True  # No empty locations.

    else:
        row = find[0]
        col = find[1]

    for i in range(1, 10):
        if check((row, col), i, board):
            board[row][col] = i

            if solve(board):  # recurse, the board with the new value added.
                return True

            board[row][col] = 0  # reset the last element that was added.

    return False  # no value 1-9 is valid for this position. Therfore we must back track.


'''
The solve method:

This method first checks for an empty space which
is represented by a 0. Then pick a number 1-9. Check
if this number that meets the constraints by calling 
the check method. If the constraints are satisfied, 
then place the number onto the board.

'''


def findEmpty(board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == 0:
                return (i, j)  # Row and Column

    return None


'''
The check method:

The method below checks the row, column 
and sector for a repeated value.

'''


def check(position, num, board):
    for i in range(len(board[0])):

        if board[position[0]][i] == num and position[
            1] != i:  # we do not want to check the position that we just inserted into.
            return False
        if board[i][position[1]] == num and position[0] != i:
            return False

    # coordinates for the sector
    boxX = position[0] // 3  # 9 numbers in total and 3 suib catagories, that is why we // 3 is used.
    boxY = position[1] // 3  # as integer divison will give a value of 0, 1 or 2.

    a = boxX * 3  # Multiply by 3 to get the coordinates of the top left box of the sector.
    b = boxY * 3

    for j in range(b, b + 3):

        if board[a][j] == num and (a, j) != position:
            return False

        if board[a + 1][j] == num and (a + 1, j) != position:
            return False

        if board[a + 2][j] == num and (a + 2, j) != position:
            return False

    return True


'''
#Note that this is a classic 9x9 classic Sudoku board.

sudokuBoard = [
    [0,9,1,2,0,0,8,3,0],
    [0,0,0,0,0,6,0,0,0],
    [0,2,0,0,0,9,0,4,7],
    [0,5,0,0,0,3,0,8,0],
    [6,0,0,4,1,0,0,0,0],
    [1,0,0,8,0,0,0,9,5],
    [0,6,0,9,0,0,0,2,0],
    [0,0,2,3,0,0,0,0,4],
    [8,3,0,0,4,0,1,6,0]
]

#solve(sudokuBoard)

'''





