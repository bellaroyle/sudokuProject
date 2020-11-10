exports.getRow = (grid, row) => {
    // function takes the sudoku grid and the index of the row we want 
    return grid[row];
    // returns the row we want 
}



exports.getColumn = (grid, column) => {
    // function takes the sudoku grid and the index of the column we want 
    const col = grid.map(row => {
        return row[column];
    })
    //pushes the number in the row with the index of the column we want, to column
    return col;
}

exports.getSquare = (grid, square) => {
    // function takes the sudoku grid and a number representing a square
    const square_coordinates = [
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
    // reference grid which shows what square each element is in 

    const inSquare = [];
    for (let row = 0; row < 9; row++) {
        for (let column = 0; column < 9; column++) {
            if (square === square_coordinates[row][column]) {
                inSquare.push(grid[row][column]);
                //goes through each number in grid, and if num has same square coordinate as square, pushes to array
            }
        }
    }
    return inSquare
    // returns an array of all the numbers in the square
}