# Leetcode 560
from typing import List

# A subarray is any contiguous part of the given array

# Approach 2: Better/Optimal solution (Generate a prefix sum and check how many prefix - k subarray exist, coz number of prefix - k == number of k)
def subarraysDivByK(nums: List[int], k: int) -> int:
    map = {}
    map[0] = 1
    prefix = 0
    count = 0

    for i in range(len(nums)):
        prefix += nums[i]
        if (prefix - k) in map:
            count += map[prefix - k] 
        if prefix in map:
            map[prefix] += 1
        else:
            map[prefix] = 1
    
    return count
    

# Approach 1: Brute force (Generate all the subsets and then check if their sum equals k)
# def subarraysDivByK(nums: List[int], k: int) -> int:
#     count = 0
#     for i in range(len(nums)):
#         for j in range(len(nums)):         
#             curr = sum(nums[i: j + 1])
#             if curr == k:
#                 count += 1
    
#     return count

nums = [1, 1, 1]
k = 2
print(subarraysDivByK(nums, k))