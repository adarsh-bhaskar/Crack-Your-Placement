# Leetcode 15

from typing import List

def twoSum(nums: List[int], target: int, left: int) -> List[int]:
    i, j = left, len(nums) - 1
    result = []

    while i < j:
        if i != left and nums[i] == nums[i - 1]:
            i += 1
        elif nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -=1
        else:
            result.append((i, j))
            i += 1
            j -= 1
    
    return result

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        result = twoSum(nums, -nums[i], i + 1)
        if result:
            for j, k in result:
                ans.append([nums[i], nums[j], nums[k]])
    
    return ans

arr = [-1, 0, 1, 2, -1, -4]
print(threeSum(arr))