# Sudoku Project

https://medium.com/javascript-in-plain-english/solve-a-sudoku-using-javascript-de456e8c34a5

## Plan: 

example of a sudoku below, will have rows indexed 0-8 and columns indexed 0-8
```
let sudoku = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
]
```

1) create helper funcs<br> 
- getRow<br>
- getColumn<br>
- getSquare<br>
- isSolved<br>
- printBoard<br>

2) create solving functions:<br>
- Brute Force 
- One value cell constraint 


```
function solve(board) {
  let updated = true, solved = false
    
  while (updated && !solved) {
    updated = one_value_cell_constraint(board)
    solved = is_solved(board)
  }
  if (!solved) {
    board = backtrack_based(board)
  }
  return board
}

```
- ^ function suggestion that uses the two solving functions to solve the board 

