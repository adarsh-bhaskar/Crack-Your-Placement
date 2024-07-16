# Leetcode 73

from typing import List

# Approach 3: Best way, Time and space optimized solution
def setZeroes(matrix: List[List[int]]) -> None:
    rowFlag, colFlag = False, False
    
    # Set markers for 1st row and 1st col
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i == 0: rowFlag = True
                if j == 0: colFlag = True
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    # Replace the inner matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    
    # Last remaining checks
    if rowFlag:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    
    if colFlag:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    
    return matrix    

# Approach 2: Better way, Time optimized solution
# def setZeroes(matrix: List[List[int]]) -> None:
#     rowFlag = [False] * len(matrix)
#     colFlag = [False] * len(matrix[0])

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 rowFlag[i] = True
#                 colFlag[j] = True
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if rowFlag[i] or colFlag[j]:
#                 matrix[i][j] = 0
    
#     return matrix

# Approach 1: Brute force (Get a list of indices where you find a zero and then loop through this list and update it to zero)
# def setZeroes(matrix: List[List[int]]) -> None:
#     indices = []

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 indices.append((i, j))
    
#     for idx in indices: # (2, 2)
#         for i in range(idx[0], idx[0] + 1):
#             for j in range(len(matrix[0])):
#                 matrix[i][j] = 0
#         for i in range(len(matrix)):
#             for j in range(idx[1], idx[1] + 1):
#                 matrix[i][j] = 0
    
#     return matrix

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeroes(matrix))