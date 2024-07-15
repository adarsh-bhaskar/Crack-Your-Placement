# https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

def findMinDiff(A, N, M):
    if N == 0 or M == 0:
        return 0
    if N < M:
        return -1
    
    A.sort()
    
    min_diff = A[N - 1] - A[0]
    
    for i in range(N - M + 1):
        min_diff = min(min_diff, A[i + M - 1] - A[i])
    
    return min_diff

A = [3, 4, 1, 9, 56, 7, 9, 12]
N = 8
M = 5
print(findMinDiff(A, N, M))