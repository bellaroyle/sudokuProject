import numpy as np 

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
sudoku = np.array([
    [7, 6, 3, 0, 0, 5, 0, 0, 9],
    [0, 1, 5, 0, 0, 2, 3, 7, 0],
    [9, 2, 8, 0, 0, 4, 0, 0, 1],
    [0, 0, 0, 5, 3, 0, 9, 8, 0],
    [0, 3, 0, 6, 0, 9, 2, 5, 0],
    [0, 0, 9, 0, 2, 0, 0, 1, 0],
    [0, 0, 0, 2, 1, 0, 7, 4, 0],
    [0, 5, 0, 4, 0, 0, 0, 3, 0],
    [0, 8, 0, 0, 5, 3, 1, 0, 0,],
])

def getRow(grid,row):
    # function takes a sudoku grid and a row index and returns the values in the row
    return grid[row]

def getColumn(grid,column):
        # function takes a sudoku grid and a column index and returns the values in the column
    col=[]
    for i in range (9):
        col.append(grid[i][column])
    return col

def getSquare(grid,row,col):
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
    ]
    square = squareCoordinates[row][col]
    inSquare=[]
    for r in range(9):
        for c in range(9):
            if (square == squareCoordinates[r][c]):
                inSquare.append(grid[r][c])
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

    rowsToCheck=[0,3,6]
    colsToCheck = [0,3,6]
    for row in rowsToCheck:
        for col in colsToCheck:
            squareSolved.append((np.sort(getSquare(grid,row,col)) == allNums).all())
    if (False in squareSolved):
        return False
    
    return True

def fillCell(grid,row,col):
    # finds all possibilities for a given, empty cell, and stores them in a sub array 
    # if only 1 possibility then fills cell
    rowContents = getRow(grid,row).tolist()
    colContents = getColumn(grid,col)
    squareContents = getSquare(grid,row,col)


    numsUsed = rowContents + colContents + squareContents
    
    possibilities = []
    for i in range(1,10):
        if (i not in numsUsed):
            possibilities.append(i)
    print(possibilities)

    if (len(possibilities) == 1):
        grid[row][col] = possibilities[0]
        return True
    else:
        grid[row][col] = np.array(possibilities)
        return False 
    