# Mask

Main idea: instead the booleans of the board indicating whether the cell contains a queen, use it to indicate "safe" cells.

so when we find a queen we set to false the cell of the queen, it line and column, and both its diagonals

so now all we have to do is iterate over the N first true cells
