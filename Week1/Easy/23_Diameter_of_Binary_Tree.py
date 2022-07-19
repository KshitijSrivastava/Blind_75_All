
# Do it Again

# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter




# Not efficient

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def length(self, root):
        if root is None:
            return 0
        
        left_len = self.length(root.left)
        right_len = self.length(root.right)
        
        return 1 + max(left_len, right_len)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_length = 0
        
        def recur(root):
            nonlocal max_length
            if root is None:
                return 
            
            left_length = self.length(root.left)
            right_length = self.length(root.right)
            
            total =  1 + left_length + right_length
            
            max_length = max(max_length, total)
            
            recur(root.left)
            recur(root.right)
            
        recur(root)
        return max_length - 1