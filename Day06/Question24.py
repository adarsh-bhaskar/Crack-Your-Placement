# Leetcode 289

from typing import List

# Original | New | State
#   0      |  0  |   0
#   0      |  1  |   1
#   1      |  0  |   2
#   1      |  1  |   3

def gameOfLife(board: List[List[int]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    def countNeighbors(r, c):
        neighbors = 0

        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                    continue
                if board[i][j] in [1, 3]:
                    neighbors += 1
        
        return neighbors
    
    for r in range(ROWS):
        for c in range(COLS):
            n = countNeighbors(r, c)

            if board[r][c]:
                if n in (2, 3):
                    board[r][c] = 3
            elif n == 3:
                board[r][c] = 2
    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in (2, 3):
                board[r][c] = 1
    
    return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))