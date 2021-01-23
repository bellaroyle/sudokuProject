import numpy as np 

def getRow(grid,row):
    # function takes a sudoku grid and a row index and returns the values in the row
    return grid[row]

def getColumn(grid,column):
        # function takes a sudoku grid and a column index and returns the values in the column
    col=[]
    for i in range (9):
        col.append(grid[i][column])
    return col

def getSquare(grid,square):
        # function takes a sudoku grid and a square index and returns the values in the square

    squareCoordinates = [
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [7, 7, 7, 8, 8, 8, 9, 9, 9],
        [7, 7, 7, 8, 8, 8, 9, 9, 9],
        [7, 7, 7, 8, 8, 8, 9, 9, 9]
    ];
    inSquare=[]
    for row in range(9):
        for column in range(9):
            if (square == squareCoordinates[row][column]):
                inSquare.append(grid[row][column])
    return inSquare

def isSolved(grid):
        # function takes a sudoku grid and checks all rows, columns and squares to see if it is solved 
        # returns a boolean
    allNums=[1,2,3,4,5,6,7,8,9]

    rowSolved = []
    colSolved = []
    squareSolved = []

    for i in range(9):
        rowSolved.append((np.sort(getRow(grid,i)) == allNums).all())
    if (False in rowSolved):
        return False

    for j in range(9):
        colSolved.append((np.sort(getColumn(grid,j)) == allNums).all())
    if (False in colSolved):
        return False

    for k in range(1,10):
        squareSolved.append((np.sort(getSquare(grid,k)) == allNums).all())
    if (False in squareSolved):
        return False
    
    return True

