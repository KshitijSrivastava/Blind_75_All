# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/balanced-binary-tree/

"""
Time : O(N ^ 2)
Space: O(N)
"""

class Solution:
    def length(self, root):
        if root is None:
            return 0
        
        left = self.length(root.left)
        right = self.length(root.right)
        
        return 1 + max(left, right)
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_len = self.length(root.left)
        right_len = self.length(root.right)
        
        if abs(left_len - right_len) > 1:
            return False
        
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        