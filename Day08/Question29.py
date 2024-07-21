# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

from typing import List

def printDuplicates(s: str) -> None:
    hashmap = {}

    for c in s:
        if c in hashmap:
            hashmap[c] += 1
        else: hashmap[c] = 1
    
    for k, v in hashmap.items():
        if v > 1:
            print(f"{k} -> {v}")

printDuplicates("test string")