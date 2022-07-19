
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
            
        self.d[key].append( (timestamp, value) )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        array = self.d[key]
        n = len(array)
        
        start = 0
        end = n - 1
        res = ""
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if array[mid][0] <= timestamp:
                res = array[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)