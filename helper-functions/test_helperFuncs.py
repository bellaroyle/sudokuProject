import unittest 
import helperFuncs
import numpy as np 

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

solvedSudoku=np.array([
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [9, 6, 5, 3, 2, 7, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 4, 6, 8, 2, 7, 1],
    [4, 7, 2, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 5],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 9, 6, 8, 2, 3],
    [2, 3, 9, 8, 4, 1, 5, 6, 7]
])


class TestHelperFuncs(unittest.TestCase):

    def test_getRow(self):
        # gets correct row
        result1 = helperFuncs.getRow(sudoku,3)
        np.testing.assert_array_equal(result1,[0, 0, 0, 5, 3, 0, 9, 8, 0])

        result2 = helperFuncs.getRow(sudoku,8)
        np.testing.assert_array_equal(result2,[0, 8, 0, 0, 5, 3, 1, 0, 0,])
    
    def test_getColumn(self):
        # gets correct column
        result1 = helperFuncs.getColumn(sudoku,3)
        np.testing.assert_array_equal(result1,[0, 0, 0, 5, 6, 0, 2, 4, 0])

        result2 = helperFuncs.getColumn(sudoku,5)
        np.testing.assert_array_equal(result2,[5, 2, 4, 0, 9, 0, 0, 0, 3])

    def test_getSquare(self):
        # gets correct square
        result1 = helperFuncs.getSquare(sudoku,1,8)
        np.testing.assert_array_equal(result1,[0, 0, 9, 3, 7, 0, 0, 0, 1])

        result2 = helperFuncs.getSquare(sudoku,7,7)
        np.testing.assert_array_equal(result2, [7, 4, 0, 0, 3, 0, 1, 0, 0])

    def test_isSolved(self):
        # returns true for a fully solved sudoku
        result1 = helperFuncs.isSolved(solvedSudoku)
        self.assertEqual(result1,True)

        # returns false for an unsolved sudoku
        result2 = helperFuncs.isSolved(sudoku)
        self.assertEqual(result2,False)

    def test_fillCell(self):
        # returns true and fills cell if only one possibility 
        testSudoku = np.array([
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
        result1 = helperFuncs.fillCell(testSudoku,0,4)
        self.assertEqual(result1, True)
        self.assertEqual(testSudoku[0][4], 8)

        # returns false and fills cell with list of possibilities if more than 1 
        testSudoku = np.array([
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
        result2 = helperFuncs.fillCell(testSudoku,0,3)
        self.assertEqual(result2, False)
        # self.assertEquals(testSudoku[0][4], [])