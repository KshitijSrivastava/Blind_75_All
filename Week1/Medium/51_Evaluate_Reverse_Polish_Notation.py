"""
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

"""

import math

class Stack():
    def __init__(self):
        self.arr = []
        
    def push(self, value):
        self.arr.append(value)
        
    def pop(self):
        return self.arr.pop()
        

class Solution:
    def math_operator(self, operator, val1, val2):
        if operator == '+':
            return int(val1) + int(val2)
        elif operator == '-':
            return int(val1) - int(val2)
        elif operator == '*':
            return int(val1) * int(val2)
        else:
            return int(val1) / int(val2)
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = Stack()
        for char in tokens:
            if char not in ['+', '-', '*', '/']:
                stack.push(int(char))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.push(self.math_operator(char, val1, val2))
                
        ans = stack.pop()
        return math.floor(ans)