# Leetcode 79

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])

    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if (r < 0 or
            c < 0 or
            r >= ROWS or
            c >= COLS or
            board[r][c] != word[i] or 
            (r, c) in path):
            return False
        
        path.add((r, c))
        result = (
            dfs(r + 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return result

    for i in range(ROWS):
        for j in range(COLS):
            if dfs(i, j, 0): return True
    
    return False

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))