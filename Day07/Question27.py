# Leetcode 84

from typing import List

# Approach 2: Better Solution
def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # A pair: (idx, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    
    return maxArea

# Approach 1: Brute Force (Try out all the possible areas in the heights array)
# def largestRectangleArea(heights: List[int]) -> int:
#     area, res = 0, 0
    
#     for i in range(len(heights)):
#         for j in range(i + 1, len(heights)):
#             area = min(heights[i: j + 1]) * (j - i + 1)
#             res = max(res, area)
    
#     return res

heights = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
print(largestRectangleArea(heights))