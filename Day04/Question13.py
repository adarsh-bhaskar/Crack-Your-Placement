# Leetcode 11

from typing import List

# Approach 1: Brute force (try every possibility using a double for loop)
def maxArea(height: List[int]) -> int:
    l, h = 0, len(height) - 1
    res = 0

    while l <= h:
        area = min(height[l], height[h]) * (h - l)
        res = max(res, area)

        if height[l] < height[h]:
            l += 1
        else:
            h -= 1
    
    return res

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))