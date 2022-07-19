
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_length(self, root):
        temp = root
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        return count
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.find_length(head)
        
        count = length - n
        
        prev = None
        temp = head
        
        while count > 0:
            prev = temp
            temp = temp.next
            count -= 1
            
        if prev is None:
            head = head.next
            del temp
            return head
        
        prev.next = temp.next
        del temp
        return head
    
    