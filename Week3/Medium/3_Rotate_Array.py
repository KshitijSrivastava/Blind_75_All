
# https://leetcode.com/problems/rotate-array/

class Solution:
    def reverse_array(self, arr, start, end):
        
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        #reverse the whole array
        self.reverse_array(nums, 0, n-1)
        
        #reverse the first k elements
        self.reverse_array(nums, 0, k-1)
    
        #revers the rest of the elements
        self.reverse_array(nums, k, n-1)
    
    """
    Time Complexity: O(N)
    Space Complexity O(N)