# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def add_node_to_head(self, node, head):
        if head is None:
            return node
        
        node.next = head
        return node
    
    def reverse_LL(self, head):
        prev = None
        
        temp = head
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            
        return prev
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = None
        
        while list1 and list2:
            
            if list1.val < list2.val:
                
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
                
            node.next = None
            new_head = self.add_node_to_head(node, new_head)
                
        while list1:
            node = list1
            list1 = list1.next
            node.next = None

            new_head = self.add_node_to_head(node, new_head)
            
        while list2:
            node = list2
            list2 = list2.next
            node.next = None

            new_head = self.add_node_to_head(node, new_head)
            
            
        new_head = self.reverse_LL(new_head)
        return new_head
                