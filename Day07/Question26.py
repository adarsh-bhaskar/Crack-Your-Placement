# Leetcode 381

import random

class RandomizedCollection:

    def __init__(self):
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            self.data.append(val)
            return False
        else:
            self.data.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        try:
            i = self.data.index(val)
            self.data.pop(i)
            return True
        except ValueError:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
val = int(input())
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()