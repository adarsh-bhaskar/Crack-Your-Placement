# Leetcode 88

from typing import List

# Approach 2: Implementing merge sort without extra space
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
        
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1

# Approach 1: Brute Force (With extra space)
# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     i, j = 0, 0
#     temp = []

#     while i < m and j < n:
#         if nums1[i] < nums2[j]:
#             temp.append(nums1[i])
#             i += 1
#         else:
#             temp.append(nums2[j])
#             j += 1
    
#     while i < m:
#         temp.append(nums1[i])
#         i += 1

#     while j < n:
#         temp.append(nums2[j])
#         j += 1
    
#     k = 0
#     for i in range(len(temp)):
#         nums1[i] = temp[k]
#         k += 1
    
#     return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)