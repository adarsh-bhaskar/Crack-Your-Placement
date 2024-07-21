# Leetcode 680

# Approach 2: Optimal Solution (O(n))
def validPalindrome(s: str) -> bool:
    def isPalindrome(s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return isPalindrome(s[l:r]) or isPalindrome(s[l + 1: r + 1])
        l += 1
        r -= 1
    
    return False

# Approach 1: Brute Force (O(n^3))
# def validPalindrome(s: str) -> bool:
#     def isPalindrome(s: str) -> bool:
#         i, j = 0, len(s) - 1

#         while i <= j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
        
#         return True

#     if isPalindrome(s):
#         return True
    
#     for i in range(len(s)):
#         if isPalindrome(s[:i] + s[i + 1:]):
#             return True
    
#     return False

s = "abcda"
print(validPalindrome(s))