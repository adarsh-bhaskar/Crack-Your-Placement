# Leetcode 493

from typing import List

# Approach 2: Optimal Solution
def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def reversePairs(nums: List[int]) -> int:
    n = len(nums)
    return mergeSort(nums, 0, n - 1)

# Approach 1: Brute Force (Generate all the pairs by running a nested for loop)
# def reversePairs(nums: List[int]) -> int:
#     res = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] > 2 * nums[j]:
#                 res.append((i, j))
    
#     return len(res)

nums = [40, 25, 19, 12, 9, 6, 2] # 6 + 3 + 3 + 2 + 1 
print(reversePairs(nums))