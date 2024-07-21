# Leetcode 14

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    ans = ""
    for i in range(len(strs[0])):
        toCompare = strs[0][i]
        match = True
        for j in range(1, len(strs)):
            if len(strs[j]) <= i or toCompare != strs[j][i]:
                match = False
                break
        
        if match == False:
            break
        else:
            ans += toCompare
        
    return ans

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))