# https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

# User function Template for python3
import math


class Solution:
    
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(s) == 0 or len(p) == 0: return 0

        map = {}
        for c in p:
            map[c] = map.get(c, 0) + 1
        
        requiredMatch = len(map)
        left = 0
        minLeft = 0
        minLength = math.inf
        matchedSoFar = 0

        for right in range(len(s)):
            c = s[right]

            if c in map:
                map[c] -= 1
                if map[c] == 0:
                    matchedSoFar += 1
                
                while matchedSoFar == requiredMatch:
                    if right - left + 1 < minLength:
                        minLeft = left
                        minLeft = right - left + 1
                    
                    leftChar = s[left]
                    if leftChar in map:
                        map[leftChar] = map.get(leftChar, 0) + 1
                        if map[leftChar] == 1:
                            matchedSoFar -= 1
                    
                    left -= 1
        if minLength == math.inf:
            return ""

        return s[minLeft: minLeft + minLength]





# Driver Code Starts

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))

# Driver Code Ends