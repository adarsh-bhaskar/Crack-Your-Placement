# https://www.geeksforgeeks.org/problems/all-unique-permutations-of-an-array/0

#User function Template for python3
from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        return list(sorted(set(permutations(arr))))

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        n = int(input())
        arr = list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j], end = " ")
            print()