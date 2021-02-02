import unittest 
import helperFuncs
import numpy as np 

sudoku = [
    [7, 6, 3, [], [], 5, [], [], 9],
    [[], 1, 5, [], [], 2, 3, 7, []],
    [9, 2, 8, [], [], 4, [], [], 1],
    [[], [], [], 5, 3, [], 9, 8, []],
    [[], 3, [], 6, [], 9, 2, 5, []],
    [[], [], 9, [], 2, [], [], 1, []],
    [[], [], [], 2, 1, [], 7, 4, []],
    [[], 5, [], 4, [], [], [], 3, []],
    [[], 8, [], [], 5, 3, 1, [], [],],
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

sudokuFilledWithPossibilities = [
    [7, 6, 3, [1, 8], 8, 5, 4, 2, 9], 
    [4, 1, 5, 9, 6, 2, 3, 7, 8], 
    [9, 2, 8, [3, 7], 7, 4, [5, 6], 6, 1], 
    [[1, 2, 6], [4, 7], [1, 2, 4, 6, 7], 5, 3, [1, 7], 9, 8, [4, 6, 7]], 
    [[1, 8], 3, [1, 4, 7], 6, 4, 9, 2, 5, 7], 
    [[5, 6, 8], [4, 7], 9, [7, 8], 2, [7, 8], 6, 1, [3, 4]], 
    [[3, 6], 9, 6, 2, 1, 8, 7, 4, 5], 
    [[1, 2], 5, [1, 2, 7], 4, 9, [6, 7], 8, 3, [2, 6]], 
    [2, 8, [4, 7], 7, 5, 3, 1, 9, 6]
]




class TestHelperFuncs(unittest.TestCase):

    def test_getRow(self):
        # gets correct row
        result1 = helperFuncs.getRow(sudoku,3)
        np.testing.assert_array_equal(result1,[ 5, 3, 9, 8])

        result2 = helperFuncs.getRow(sudoku,8)
        np.testing.assert_array_equal(result2,[ 8, 5, 3, 1])
    
    def test_getColumn(self):
        # gets correct column
        result1 = helperFuncs.getColumn(sudoku,3)
        np.testing.assert_array_equal(result1,[5, 6, 2, 4])

        result2 = helperFuncs.getColumn(sudoku,5)
        np.testing.assert_array_equal(result2,[5, 2, 4, 9, 3])

    def test_getSquare(self):
        # gets correct square
        result1 = helperFuncs.getSquare(sudoku,1,8)
        np.testing.assert_array_equal(result1,[9, 3, 7, 1])

        result2 = helperFuncs.getSquare(sudoku,7,7)
        np.testing.assert_array_equal(result2, [7, 4, 3, 1])

    def sudokuIsFilled(self):
        # returns true for a sudoku full of just numbers 
        result1 = helperFuncs.getSquare(solvedSudoku)
        self.assertEqual(result1,True)

        # returns false for a sudoku with sub lists 
        result2 = helperFuncs.getSquare(sudoku)
        self.assertEqual(result2,False)

        # returns false for a sudoku where all the cells are filled with either int or list 
        result3 = helperFuncs.sudokuisFilled(sudokuFilledWithPossibilities)
        self.asserEqual(result3,False)

    def test_isSolved(self):
        # returns true for a fully solved sudoku
        result1 = helperFuncs.isSolved(solvedSudoku)
        self.assertEqual(result1,True)

        # returns false for an unsolved sudoku
        result2 = helperFuncs.isSolved(sudoku)
        self.assertEqual(result2,False)

        # returns false for a sudoku where all the cells are filled with either int or list 
        result3 = helperFuncs.isSolved(sudokuFilledWithPossibilities)
        self.assertEqual(result3,False)

        # returns false for an incorrectly completed sudoku
        incorrectlySolved = [
            [1, 2, 7, 1, 5, 4, 3, 9, 6],
            [9, 6, 5, 3, 2, 7, 1, 4, 8],
            [3, 4, 1, 6, 8, 9, 7, 5, 2],
            [5, 9, 3, 4, 6, 8, 2, 7, 1],
            [4, 7, 2, 5, 1, 3, 6, 8, 9],
            [6, 1, 8, 9, 7, 2, 4, 3, 5],
            [7, 8, 6, 2, 3, 5, 9, 1, 4],
            [1, 5, 4, 7, 9, 6, 8, 2, 3],
            [2, 3, 9, 8, 4, 1, 5, 6, 7]
        ]
        result4 = helperFuncs.isSolved(incorrectlySolved)
        self.assertEqual(result4,False)

    def test_fillCell(self):
        # returns true and fills cell if only one possibility 
        testSudoku = [
            [7, 6, 3, [], [], 5, [], [], 9],
            [[], 1, 5, [], [], 2, 3, 7, []],
            [9, 2, 8, [], [], 4, [], [], 1],
            [[], [], [], 5, 3, [], 9, 8, []],
            [[], 3, [], 6, [], 9, 2, 5, []],
            [[], [], 9, [], 2, [], [], 1, []],
            [[], [], [], 2, 1, [], 7, 4, []],
            [[], 5, [], 4, [], [], [], 3, []],
            [[], 8, [], [], 5, 3, 1, [], [],],
        ]
        result1 = helperFuncs.fillCell(testSudoku,0,4)
        self.assertEqual(result1, True)
        self.assertEqual(testSudoku[0][4], 8)

        # returns false and fills cell with list of possibilities if more than 1 
        testSudoku = [
            [7, 6, 3, [], [], 5, [], [], 9],
            [[], 1, 5, [], [], 2, 3, 7, []],
            [9, 2, 8, [], [], 4, [], [], 1],
            [[], [], [], 5, 3, [], 9, 8, []],
            [[], 3, [], 6, [], 9, 2, 5, []],
            [[], [], 9, [], 2, [], [], 1, []],
            [[], [], [], 2, 1, [], 7, 4, []],
            [[], 5, [], 4, [], [], [], 3, []],
            [[], 8, [], [], 5, 3, 1, [], [],],
        ]
        result2 = helperFuncs.fillCell(testSudoku,0,3)
        self.assertEqual(result2, False)
        self.assertEqual(testSudoku[0][3], [1,8])


    def test_fillGrid(self):
        # returns the suduku with each cell filled with either an int or list length > 0
        testSudoku = [
            [7, 6, 3, [], [], 5, [], [], 9],
            [[], 1, 5, [], [], 2, 3, 7, []],
            [9, 2, 8, [], [], 4, [], [], 1],
            [[], [], [], 5, 3, [], 9, 8, []],
            [[], 3, [], 6, [], 9, 2, 5, []],
            [[], [], 9, [], 2, [], [], 1, []],
            [[], [], [], 2, 1, [], 7, 4, []],
            [[], 5, [], 4, [], [], [], 3, []],
            [[], 8, [], [], 5, 3, 1, [], [],],
        ]
        filled = helperFuncs.fillGrid(testSudoku)
        for row in range(9):
            for col in range(9):
                cell = filled[row][col]
                if (isinstance(cell, list)):
                    assert(len(cell)>0)
                else:
                    assert(isinstance(cell,int))
                
    
    def test_completeSudoku(self):
        #  returns completed sudoku
        testSudoku = [
            [7, 6, 3, [], [], 5, [], [], 9],
            [[], 1, 5, [], [], 2, 3, 7, []],
            [9, 2, 8, [], [], 4, [], [], 1],
            [[], [], [], 5, 3, [], 9, 8, []],
            [[], 3, [], 6, [], 9, 2, 5, []],
            [[], [], 9, [], 2, [], [], 1, []],
            [[], [], [], 2, 1, [], 7, 4, []],
            [[], 5, [], 4, [], [], [], 3, []],
            [[], 8, [], [], 5, 3, 1, [], [],],
        ]
        result1 = helperFuncs.completeSudoku(testSudoku)
        self.assertEqual(helperFuncs.isSolved(result1) , True)