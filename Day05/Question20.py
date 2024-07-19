# Leetcode 55

from typing import List

# Approach 2: Optimal (Greedy linear time)
def canJump(nums: List[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return False if goal else True

# Approach 1: Brute Force
# def canJump(nums: List[int]) -> bool:
#     if len(nums) == 1:
#         return True
            
#     def helper(nums, l, h):
#         if l == h:
#             return 0
        
#         if nums[l] == 0:
#             return float('inf')

#         minVal = float('inf')
#         for i in range(l + 1, h + 1):
#             if i < l + nums[l] + 1:
#                 jumps = helper(nums, i, h)
#                 if jumps != float('inf') and jumps + 1 < minVal:
#                     minVal = jumps + 1
        
#         return minVal

#     if helper(nums, 0, len(nums) - 1) == 0 or helper(nums, 0, len(nums) - 1) == float("inf"):
#             return False
#     return True

nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
print(canJump(nums))