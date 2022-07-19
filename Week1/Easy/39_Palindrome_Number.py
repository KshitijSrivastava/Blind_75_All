
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        temp = x
        
        while temp:
            q = temp % 10
            temp = temp // 10
            rev = (rev * 10) + q
            
        return rev == x