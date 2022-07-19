
# https://leetcode.com/problems/insert-interval/

"""
Case 1
        -------- ---------
----        
        
Case 2

-------   ---  ----------
     ------
     
Case 3

------    ------  ---------

    ----------------
    
    
Case 4

------             ----------

        -------
        
Case 5

-------      ------------ 
                            ----------

"""

class Solution:
    def merge_intervals(self, intervals):
        n = len(intervals)
        
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        
        output = []
        
        for i in range(1, n):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            
            #no intersection
            if prev_end < curr_start:
                output.append( [prev_start, prev_end] )
                prev_start = curr_start
                prev_end = curr_end
            #intersection in the intervals
            else:
                prev_start = min(prev_start, curr_start)
                prev_end = max(prev_end, curr_end)
                
        output.append( [prev_start, prev_end] )
        return output
                
            
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort( key = lambda x: x[0] )
        
        n = len(intervals)
        output = []
        
        if newInterval == []:
            return self.merge_intervals(intervals)
        
        s_newInterval = newInterval[0]
        e_newInterval = newInterval[1]
        
        inserted = False
        for i in range(n):
            if intervals[i][0] > s_newInterval:
                intervals.insert( i, newInterval )
                inserted = True
                
        if inserted == False:
            intervals.append(newInterval)
            inserted =  True
            
        return self.merge_intervals(intervals)
            
        