# Leetcode 1423

from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    lsum, rsum = 0, 0
    maxSum = 0

    for i in range(k):
        lsum += cardPoints[i]
    
    maxSum = lsum
    rightIdx = len(cardPoints) - 1
    for i in range(k - 1, -1, -1):
        lsum -= cardPoints[i]
        rsum += cardPoints[rightIdx]
        maxSum = max(maxSum, lsum + rsum)
        rightIdx -= 1
    
    return maxSum

cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
print(maxScore(cardPoints, k))