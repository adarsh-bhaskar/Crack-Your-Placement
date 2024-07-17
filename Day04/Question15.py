# Leetcode 18

from typing import List

# Approach 3: Optimal Solution
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    N = len(nums)
    res = []

    for i in range(N):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, N):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k, l = j + 1, N - 1
            while k < l:
                curr = nums[i] + nums[j] + nums[k] + nums[l]
                if curr == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]: k += 1
                    while k < l and nums[l] == nums[l + 1]: l -= 1
                elif curr < target:
                    k += 1
                else:
                    l -= 1
    
    return res              


# Approach 2: Better solution
# def fourSum(nums: List[int], target: int) -> List[List[int]]:
#     N = len(nums)
#     res = []

#     for i in range(N):
#         for j in range(i + 1, N):
#             hashset = set()
#             for k in range(j + 1, N):
#                 curr = nums[i] + nums[j]
#                 curr += nums[k]

#                 complement = target - curr

#                 if complement in hashset:
#                     temp = [nums[i], nums[j], nums[k], complement]
#                     temp.sort()
#                     if temp not in res:
#                         res.append(temp)
#                 hashset.add(nums[k])
    
#     return res

# Approach 1: Brute force (Generate all the quads by running 4 nested loops)
# def fourSum(nums: List[int], target: int) -> List[List[int]]:
#     N = len(nums)
#     res = []

#     for i in range(N):
#         for j in range(i + 1, N):
#             for k in range(j + 1, N):
#                 for l in range(k + 1, N):
#                     curr = nums[i] + nums[j]
#                     curr += nums[k]
#                     curr += nums[l]
#                     temp = []
#                     if curr == target:
#                         temp.append(nums[i])
#                         temp.append(nums[j])
#                         temp.append(nums[k])
#                         temp.append(nums[l])
#                         temp.sort()
#                         res.append(temp)
    
#     return res

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))