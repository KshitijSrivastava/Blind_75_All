


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def recur(start, end):
            if start > end:
                return None
            
            mid = (start + end)// 2
            #print(start, end, mid)
            
            node = TreeNode( nums[mid] )
            node.left = recur(start, mid - 1)
            node.right = recur(mid + 1, end)
            
            return node
        
        return recur(0, len(nums)-1)
        
        
            