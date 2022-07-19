


# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        
        def recur(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            
            return recur(root1.left, root2.right) and recur(root1.right, root2.left)
        
        return recur(root, root)