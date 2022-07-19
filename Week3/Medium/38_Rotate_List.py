# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length_LL(self, head):
        count = 0
        
        temp = head
        
        while temp:
            temp = temp.next
            count += 1
        return count
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = self.length_LL(head)
        
        if length == 0:
            return None
        k = k % length
        if k == 0:
            return head
        
        prev = None
        
        node_count = length - k
        temp = head
        while node_count:
            prev = temp
            temp = temp.next
            node_count -= 1
        
        prev.next = None
        
        last_node = temp
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = head
        return temp