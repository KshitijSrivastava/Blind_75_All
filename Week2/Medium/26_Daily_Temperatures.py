
#https://leetcode.com/problems/daily-temperatures/

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = []
        stack = []
        
        for idx in range(n-1, -1, -1):
            num = temperatures[idx]
            #print(idx, num)
            
            while len(stack) != 0:
                if stack[-1].value > num:
                    break
                stack.pop()
            
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(stack[-1].index - idx)
            stack.append( Node(num, idx) )
            
        return output[::-1]
                
            