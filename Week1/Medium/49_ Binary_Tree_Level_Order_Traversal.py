# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = {}
        max_level = -1
        
        def recur(node, level):
            nonlocal d, max_level
            if node is None:
                return 
            
            max_level = max(max_level, level)
            
            if level not in d:
                d[level] = []
            d[level].append( node.val )
            
            recur(node.left, level + 1)
            recur(node.right, level + 1)
        
        recur(root, 0)
        output = []
        
        for lv in range(0, max_level+1):
            output.append( d[lv] )
        return output
        