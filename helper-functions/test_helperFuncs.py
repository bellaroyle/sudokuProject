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



class TestHelperFuncs(unittest.TestCase):

    def test_getRow(self):
        result1 = helperFuncs.getRow(sudoku,3)
        np.testing.assert_array_equal(result1,[0, 0, 0, 5, 3, 0, 9, 8, 0])

        result2 = helperFuncs.getRow(sudoku,8)
        np.testing.assert_array_equal(result2,[0, 8, 0, 0, 5, 3, 1, 0, 0,])
    
    def test_getColumn(self):
        result1 = helperFuncs.getColumn(sudoku,3)
        np.testing.assert_array_equal(result1,[0, 0, 0, 5, 6, 0, 2, 4, 0])

        result2 = helperFuncs.getColumn(sudoku,5)
        np.testing.assert_array_equal(result2,[5, 2, 4, 0, 9, 0, 0, 0, 3])

    def test_getSquare(self):
        result1 = helperFuncs.getSquare(sudoku,3)
        np.testing.assert_array_equal(result1,[0, 0, 9, 3, 7, 0, 0, 0, 1])

        result2 = helperFuncs.getSquare(sudoku,9)
        np.testing.assert_array_equal(result2,[7, 4, 0, 0, 3, 0, 1, 0, 0])