

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
(node, number)
            (1,0)
        (3,1)    (2,2)
    (5,3) (3,4)     (9,5)

"""


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        
        queue = []
        queue.append( (root, 0, 0) )
        
        max_width = 0
        left_value = {}
        
        while queue:
            node, value, level = queue.pop(0)
            
            
            if level not in left_value:
                left_value[level] = float('inf')
                
            left_value[level] = min(left_value[level], value)
            
            width = value - left_value[level]
            max_width = max(max_width, width)
            
            #print(max_width, width, left_value)
            
            if node.left:
                queue.append( (node.left, (value*2) + 1, level + 1) )
            
            if node.right:
                queue.append( (node.right, (value * 2) + 2, level + 1) )
                
        return max_width + 1
                
            