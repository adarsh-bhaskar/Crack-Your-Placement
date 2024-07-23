# https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

# User function Template for python3

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    
    
    def smallestWindow(self, s, p):
        no_of_chars = 256
        
        len1 = len(s)
        len2 = len(p)
    
        # Check if string's length is
        # less than pattern's
        # length. If yes then no such
        # window can exist
        if len1 < len2:
            return -1
    
        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars
    
        # Store occurrence ofs characters of pattern
        for i in range(0, len2):
            hash_pat[ord(p[i])] += 1
    
        start, start_index, min_len = 0, -1, float('inf')
    
        # Start traversing the string
        count = 0  # count of characters
        for j in range(0, len1):
    
            # count occurrence of characters of string
            hash_str[ord(s[j])] += 1
    
            # If string's char matches with
            # pattern's char then increment count
            if (hash_str[ord(s[j])] <=
                    hash_pat[ord(s[j])]):
                count += 1
    
            # if all the characters are matched
            if count == len2:
    
                # Try to minimize the window
                while (hash_str[ord(s[start])] >
                       hash_pat[ord(s[start])] or
                       hash_pat[ord(s[start])] == 0):
    
                    if (hash_str[ord(s[start])] >
                            hash_pat[ord(s[start])]):
                        hash_str[ord(s[start])] -= 1
                    start += 1
    
                # update window size
                len_window = j - start + 1
                if min_len > len_window:
    
                    min_len = len_window
                    start_index = start
    
        # If no window found
        if start_index == -1:
            return -1
    
        # Return substring starting from
        # start_index and length min_len
        return s[start_index: start_index + min_len]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
# } Driver Code Ends