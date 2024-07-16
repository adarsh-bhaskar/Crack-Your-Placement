# Leetcode 442

from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    hashset = set()
    answer = []

    for num in nums:
        if num in hashset:
            answer.append(num)
        hashset.add(num)

    return answer

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))