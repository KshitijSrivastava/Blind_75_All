

# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_to_head(self, head, node):
        if head is None:
            return node
        node.next = head
        return node
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = []
        
        while head:
            node = head
            head = head.next
            node.next = None
            
            lst.append(node)
            
        lst.sort( reverse = True, key = lambda x: x.val )
        
        new_head = None
        
        for node in lst:
            new_head = self.add_to_head(new_head, node)
            
        return new_head
        