from typing import List

def removeDuplicates(nums: List[int]) -> int:
    hashmap = {}
    count = 0

    for num in nums:
        if num not in hashmap:
            hashmap[num] = count
            nums[count] = num
            count += 1
    
    return count

nums = [1, 1, 2]
print(removeDuplicates(nums))