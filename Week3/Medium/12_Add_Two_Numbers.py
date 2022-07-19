
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_at_head(self, head, val):
        new_node = ListNode(val)
        
        if head is None:
            return new_node
        
        new_node.next = head
        return new_node
        
        
    def reverse_LL(self, head):
        
        prev = None
        
        temp = head
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        
        temp1 = l1
        temp2 = l2
        
        new_head = None
        
        while temp1 and temp2:
            
            total = carry + temp1.val + temp2.val
            val = total % 10
            carry = total // 10
            
            #print(val, carry)
            
            new_head = self.add_at_head(new_head, val)
            
            temp1 = temp1.next
            temp2 = temp2.next
            
        
        while temp1:
            total = carry + temp1.val
            val = total % 10
            carry = total // 10
            
            new_head = self.add_at_head(new_head, val)
            temp1 = temp1.next
            
            
        while temp2:
            total = carry + temp2.val
            val = total % 10
            carry = total // 10
            
            new_head = self.add_at_head(new_head, val)
            temp2 = temp2.next
            
        if carry != 0:
            new_head = self.add_at_head(new_head, carry)
            
        return self.reverse_LL(new_head)