# Leetcode 75

from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Insertion Sort Algorithm:    
    insertionSort(array)
    mark first element as sorted
    for each unsorted element X
        'extract' the element X
        for j <- lastSortedIndex down to 0
        if current element j > X
            move sorted element to the right by 1
        break loop and insert X here
    end insertionSort
    """
    for step in range(1, len(nums)):
        key = nums[step]
        j = step - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key

nums = [9, 5, 1, 4, 3]
sortColors(nums)
print(nums)