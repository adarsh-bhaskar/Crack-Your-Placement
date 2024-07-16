# Leetcode 974
from typing import List
from collections import defaultdict

# A subarray is any contiguous part of the given array

# Generate a prefix-sum of remainders. If the remainder is in the map then count
#  else enter the remainder to the map

def subarrayDivByK(nums: List[int], k: int):
    map = defaultdict(int)
    map[0] = 1
    prefix = 0
    count = 0

    for num in nums:
        prefix += num
        remainder = prefix % k

        if remainder in map:
            count += map[remainder]
        map[remainder] += 1
    
    return count

nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarrayDivByK(nums, k))