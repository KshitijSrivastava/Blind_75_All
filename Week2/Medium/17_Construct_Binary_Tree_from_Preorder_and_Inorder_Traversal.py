

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

porder = [3,9,20,15,7]
iorder = [9,3,15,20,7]

     []            [9]   <- 3 - >         [15,20,7] 

"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        
        node_val = preorder[0]
        
        node_index_inorder = inorder.index(node_val)
        
        root = TreeNode( node_val )
        root.left = self.buildTree( preorder[1:node_index_inorder + 1]  , inorder[0:node_index_inorder] )
        root.right = self.buildTree( preorder[node_index_inorder + 1: ]  , inorder[node_index_inorder + 1: ])
        
        return root