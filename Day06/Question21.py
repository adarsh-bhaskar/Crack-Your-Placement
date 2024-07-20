# Leetcode 169

from typing import List

def majorityElement(nums: List[int]) -> int:
    hashmap = {}

    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        hashmap[num] = 1
    
    res = 0
    for key in hashmap.keys():
        if hashmap[key] >= len(nums) // 2:
            res = key
    
    return res

nums = [3, 2, 3]
print(majorityElement(nums))