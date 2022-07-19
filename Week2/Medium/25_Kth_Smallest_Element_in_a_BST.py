


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = None
        idx = 0
        
        def recur(root):
            nonlocal ans, idx
            
            if root is None:
                return 
            
            recur(root.left)
            
            idx += 1
            
            if idx == k:
                ans = root.val
                return
            
            recur(root.right)
            
        recur(root)
        return ans