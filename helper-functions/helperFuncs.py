import numpy as np 

a = np.array([
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

# print(a[1])


def getRow(grid,row):
    return grid[row]

def getColumn(grid,column):
    col=[]
    for i in range (9):
        col.append(a[i][column])
    return col

def getSquare(grid,square):
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


