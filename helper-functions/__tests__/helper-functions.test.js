
const { getRow, getColumn, getSquare } = require('../helper-functions')

const testGrid = [
    [7, 6, 3, 0, 0, 5, 0, 0, 9],
    [0, 1, 5, 0, 0, 2, 3, 7, 0],
    [9, 2, 8, 0, 0, 4, 0, 0, 1],
    [0, 0, 0, 5, 3, 0, 9, 8, 0],
    [0, 3, 0, 6, 0, 9, 2, 5, 0],
    [0, 0, 9, 0, 2, 0, 0, 1, 0],
    [0, 0, 0, 2, 1, 0, 7, 4, 0],
    [0, 5, 0, 4, 0, 0, 0, 3, 0],
    [0, 8, 0, 0, 5, 3, 1, 0, 0,],
]

describe('getRow', () => {
    test('returns the correct row ', () => {
        expect(getRow(testGrid, 5)).toEqual([0, 0, 9, 0, 2, 0, 0, 1, 0])
    });
    test('does not mutate input', () => {
        getRow(testGrid, 5);
        expect(testGrid).toEqual([
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
    });
});

describe('getColumn', () => {
    test('returns the correct column', () => {
        expect(getColumn(testGrid, 4)).toEqual([0, 0, 0, 3, 0, 2, 1, 0, 5])
    });
    test('does not mutate input', () => {
        getColumn(testGrid, 5);
        expect(testGrid).toEqual([
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
    });
});

describe('getSquare', () => {
    test('returns array of numbers in the same square', () => {
        expect(getSquare(testGrid, 3)).toEqual([0, 0, 9, 3, 7, 0, 0, 0, 1])
    });
    test('does not mutate input', () => {
        getSquare(testGrid, 5);
        expect(testGrid).toEqual([
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
    });
});
