

# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        
        self.arr = []
        self.mini = []
        

    def push(self, val: int) -> None:
        
        minimum = float('inf')
        
        if len(self.arr) != 0:
            minimum = self.arr[-1][1]
            
        self.arr.append( ( val, min(minimum, val) ) )
        

    def pop(self) -> None:
        value = self.arr.pop()[0]
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()