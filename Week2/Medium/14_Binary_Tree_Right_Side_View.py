

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Queue

[  (1,0), (3,1), (2,1), (4,2), (5,2) ]

"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        curr_level = 0
        
        if root is None:
            return output
        
        queue = []
        queue.append( (root, 0) )
        
        
        while queue:
            
            node, level = queue.pop(0)
            
            if curr_level == level:
                output.append(node.val)
                curr_level += 1
            
            if node.right:
                queue.append( (node.right, level + 1) )
                
            if node.left:
                queue.append( (node.left, level + 1) )
                
        return output