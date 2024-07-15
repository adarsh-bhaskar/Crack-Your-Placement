# Leetcode 1

from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    N = len(nums)

    for i in range(N):
        complement = target - nums[i]

        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))