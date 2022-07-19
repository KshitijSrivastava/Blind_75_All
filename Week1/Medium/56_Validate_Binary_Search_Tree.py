# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

 #https://leetcode.com/problems/validate-binary-search-tree



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(root, maximum, minimum):
            if root is None:
                return True
            
            if root.val >= maximum or root.val <= minimum:
                return False
            
            return recur(root.left, root.val, minimum) and recur(root.right, maximum, root.val)
        
        
        return recur(root, float('inf'), float('-inf'))