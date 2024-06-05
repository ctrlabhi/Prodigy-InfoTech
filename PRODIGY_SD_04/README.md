# PRODIGY_SD_04
Implement a Sudoku Solver

In the Sudoku puzzle, we need to fill in every empty box with an integer between 1 and 9 in such a way that every number from 1 up to 9 appears once in every row, every column, and every one of the small 3 by 3 boxes highlighted with thick borders.

The difficulty of this puzzle might vary. The more the difficulty level of Sudoku puzzles, the more challenging the research problem it becomes for computational scientists. Difficult puzzles mostly have less prescribed symbols.

The Sudoku puzzles which are published for entertainment have unique solutions. A Sudoku puzzle is believed to be well-formed if it has a unique solution. Another challenging research problem is to determine how few boxes need to be filled for a Sudoku puzzle to be well-formed. Well-formed Sudoku with 17 symbols exists. It is unknown whether or not there exists a well-formed puzzle with only 16 clues. The lesser the clues, the higher the chances of multiple solutions.

Steps to solve the Sudoku Puzzle in Python:

1. In this method for solving the sudoku puzzle, first, we assign the size of the 2D matrix to a variable M (M*M).

2. Then we assign the utility function (puzzle) to print the grid.

3. Later it will assign num to the row and col.

4. If we find the same num in the same row or same column or in the specific 3*3 matrix, ‘false’ will be returned.

5. Then we will check if we have reached the 8th row and 9th column and return true for stopping further backtracking.

6. Next, we will check if the column value becomes 9 then we move to the next row and column.

7. Further now we see if the current position of the grid has a value greater than 0, then we iterate for the next column.

8. After checking if it is a safe place, we move to the next column and then assign the num in the current (row, col) position of the grid. Later we check for the next possibility with the next column.

9. As our assumption was wrong, we discard the assigned num and then we go for the next assumption with a different num value

Implementing the Sudoku Solver in Python:

We’ll use the backtracking method to create our sudoku solver in Python. Backtracking means switching back to the previous step as soon as we determine that our current solution cannot be continued into a complete one. We use this principle of backtracking to implement the sudoku algorithm. It’s also called the brute force algorithm way to solve the sudoku puzzle.

Features:

Provides a 9x9 grid for entering Sudoku puzzle numbers.
Includes a "Solve" button to solve the entered puzzle.
Displays an error message if the puzzle has no solution.
Highlights the solved puzzle on the grid.