import random

"""

# https://leetcode.com/problems/insert-delete-getrandom-o1/

1:0
[1]

1:0, 2:1
[1,2]



"""


class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.arr = []
        self.idx = -1

    def insert(self, val: int) -> bool:
        # if the value is in self.d
        # return False
        if val in self.d:
            return False
        
        self.idx += 1
        
        self.d[val] = self.idx
        self.arr.append(val)
        
        
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        """
        1:0, 2:1
        [1,2]

        """
        removed_val_index = self.d[val]
        
        last_index_val = self.arr[-1]
        self.arr[removed_val_index] = last_index_val
        
        self.arr.pop()
        
        self.d[last_index_val] = removed_val_index
        
        del self.d[val]
        self.idx -= 1
        
        return True
        

    def getRandom(self) -> int:
        random_index = random.randint( 0, len(self.arr) - 1 )
        
        return self.arr[random_index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()