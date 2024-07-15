# Leetcode 283

from typing import List

def moveZeroes(nums: List[int]) -> None:
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
    
    for i in range(j, len(nums)):
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)