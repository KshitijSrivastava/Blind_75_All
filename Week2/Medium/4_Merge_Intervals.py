

# https://leetcode.com/problems/merge-intervals/



"""

Case1: No overlap
------
        ------
        
Case 2: Overlap
-------
    --------
    
case3: Overlap

-----------
    ----

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        output = []
        
        if n == 0:
            return output
        
        intervals.sort(key = lambda x : x[0])
        
        prev_start = None
        prev_end = None
        
        for i, interval in enumerate(intervals):
            if i == 0:
                prev_start = interval[0]
                prev_end = interval[1]
                continue
            curr_start = interval[0]
            curr_end = interval[1]
                
            if prev_end < curr_start:
                output.append( [prev_start, prev_end] )
                prev_start = curr_start
                prev_end = curr_end
            else:
                prev_end = max(prev_end, curr_end)
                
        output.append( [prev_start, prev_end] )
        
        return output
                
            
                