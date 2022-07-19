import heapq
import math

"""

            Min heap
            
            0
        1       3
        
    4      5
    
    
            Max heap
            -5
        -4     -3
    -1     0
    
    if new object is less then -5 (heap top) ignore
    else remove the heap top element
        
"""


class Node:
    def __init__(self, point, distance):
        self.distance = distance
        self.point = point
        
    def __gt__(self, other):
        return self.distance > other.distance
    
    def __gte__(self, other):
        return self.distance >= other.distance
    
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __lte__(self, other):
        return self.distance <= other.distance

class Solution:
    def distance(self, x, y):
        return sqrt( (x * x) + (y * y) )
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #k minimum distances
        
        maxHeap = []
        for pt in points:
            
            obj = Node(pt,  -1 * self.distance(pt[0], pt[1]) )
            
            if len(maxHeap) < k:
                heapq.heappush( maxHeap, obj )
                
            else:
                
                if obj < maxHeap[0]:
                    pass
                else:
                    heapq.heappop(maxHeap)
                    heapq.heappush( maxHeap, obj )
                    
        output = []
        
        for obj in maxHeap:
            output.append( obj.point )
        return output
                    
                
        