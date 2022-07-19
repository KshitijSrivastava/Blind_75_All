

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, arr, index):
        
        n = len(arr[index])
        
        i = 0
        j = n - 1
        
        while i < j:
            arr[index][i], arr[index][j] = arr[index][j], arr[index][i]
            i += 1
            j -= 1
            
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        
        if root is None:
            return output
        
        queue = []
        queue.append( (root, 0) )
        
        
        while queue:
            node, level = queue.pop(0)
            
            if node is None:
                continue
            
            if len(output) <= level:
                #print(output , node.val, level)
                output.append([])
            
            output[level].append(node.val)
            
            if node.left:
                queue.append( (node.left, level + 1) )
                
            if node.right:
                queue.append( (node.right, level + 1) )
                
        
        height = len(output)
        
        for i in range(height):
            if i % 2 == 1:
                self.reverse(output, i)
        return output
        