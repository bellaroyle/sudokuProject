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
sudoku = [
    [7, 6, 3, [], [], 5, [], [], 9],
    [[], 1, 5, [], [], 2, 3, 7, []],
    [9, 2, 8, [], [], 4, [], [], 1],
    [[], [], [], 5, 3, [], 9, 8, []],
    [[], 3, [], 6, [], 9, 2, 5, []],
    [[], [], 9, [], 2, [], [], 1, []],
    [[], [], [], 2, 1, [], 7, 4, []],
    [[], 5, [], 4, [], [], [], 3, []],
    [[], 8, [], [], 5, 3, 1, [], []],
]

solvedSudoku=[
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [9, 6, 5, 3, 2, 7, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 4, 6, 8, 2, 7, 1],
    [4, 7, 2, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 5],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 9, 6, 8, 2, 3],
    [2, 3, 9, 8, 4, 1, 5, 6, 7]
]

def getRow(grid,row):
    # function takes a sudoku grid and a row index and returns the values in the row
    rowContents=[]
    for i in range (9):
        if (not grid[row][i] == []):
            rowContents.append(grid[row][i])

    return rowContents



def getColumn(grid,column):
        # function takes a sudoku grid and a column index and returns the values in the column
    col=[]
    for i in range (9):
        if (not grid[i][column] == []):
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
            if (square == squareCoordinates[r][c] and not grid[r][c] == [] ):
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
        if ( not len(getRow(grid,i)) == 9):
            return False

    for j in range(9):
        if ( not len(getColumn(grid,i)) == 9):
            return False


    rowsToCheck=[0,3,6]
    colsToCheck = [0,3,6]
    for row in rowsToCheck:
        for col in colsToCheck:
            if( not len(getSquare(grid,row,col)) == 9):
                return False
    
    return True



def fillCell(grid,row,col):
    # finds all possibilities for a given, empty cell, and stores them in a sub array 
    # if only 1 possibility then fills cell
    rowContents = getRow(grid,row) #.tolist()
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
        grid[row][col] = possibilities
        print(grid[row][col])
        
        return False 
print(fillCell(sudoku,0,3))
print(sudoku)