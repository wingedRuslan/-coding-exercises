"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Idea: 1 pass through the board
            - keep track of unique elements in each row / col / square
            (collections.defaultdict(set))
            - ! each square has its indices (i, j): i = row / 3, j = col / 3
            allows to uniquely identify a 3x3 square within board
        
        Tricky part - how to keep track of unique elements in each square
            -> assign each square has its indices (i, j): i = row / 3, j = col / 3
        
        Time: O(9*9), num_rows * num_cols
        Space: O(9*9)
        """

        rows = collections.defaultdict(set)     # key = row
        cols = collections.defaultdict(set)     # key = col
        squares = collections.defaultdict(set)  # key = (row / 3, col / 3)

        num_rows = len(board)
        num_cols = len(board[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == '.':
                    continue
                
                # Violation of the sudoku rules
                if (
                    board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row // 3, col // 3)]
                ):
                    return False
                
                # Track unique digits in rows / cols / squares
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True

