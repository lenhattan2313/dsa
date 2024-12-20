from random import random


class Solution:
    def __init__(self):
        self.data = []
        self.data_map = {}

    def insert(self, val):
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        if val not in self.data_map:
            return False
        last_val = self.data[-1]
        index_remove = self.data_map[val]

        self.data_map[last_val] = index_remove
        self.data[index_remove] = last_val

        self.data.pop()
        self.data_map.pop(val)
        return True

    def randomVal(self):
        return random.choice(self.data)


