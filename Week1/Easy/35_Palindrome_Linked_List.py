
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self, head):
        
        prev = None
        temp = head
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev
    
    def print_LL(self, root):
        
        arr = []
        
        temp = root
        while temp:
            arr.append( str( temp.val) )
            temp = temp.next
            
        return "->".join(arr)
        
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        prev = None
        
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev is not None:
            prev.next = None
            
        slow = self.reverse_LL(slow)
            # 1->2->3->4->5 
        temp = head
        # print(self.print_LL(head))
        # print(self.print_LL(slow))
        while slow and temp:
            print(slow.val, temp.val)
            if slow.val != temp.val:
                return False
            slow = slow.next
            temp = temp.next
        return True
            
        