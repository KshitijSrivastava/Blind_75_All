
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        
        while self.stack1:
            
            val = self.stack1.pop()
            self.stack2.append( val )
        #remove the element
        element = self.stack2.pop()
        
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append( val )
            
        return element
            
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()