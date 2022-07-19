
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        if root == p:
            return root
        elif root == q:
            return root
        left_return_value = self.lowestCommonAncestor(root.left, p, q)
        right_return_value = self.lowestCommonAncestor(root.right, p, q)
        
        if left_return_value is None and right_return_value is None:
            return None
        elif left_return_value is not None and right_return_value is None:
            return left_return_value
        elif left_return_value is None and right_return_value is not None:
            return right_return_value
        else:
            return root