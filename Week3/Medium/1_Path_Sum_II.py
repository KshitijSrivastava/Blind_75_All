
# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        output = []
        
        if root is None:
            return output
        
        def recur(root, curr, target):
            if root.left is None and root.right is None:
                
                if target == root.val:
                    curr.append(root.val)
                    output.append( curr[::] )
                    curr.pop()
                    
                return
            
            curr.append( root.val )
            
            target -= root.val
            
            if root.left:
                recur(root.left, curr, target)
                
            if root.right:
                recur(root.right, curr, target)
                
            curr.pop()
            
        recur(root, [], targetSum)
        return output