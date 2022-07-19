"""

# https://leetcode.com/problems/top-k-frequent-words/

O(N) Space COmplexity And O(N) time complexity
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        
        d = {}
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
            
        count = [ [] for i in range(n) ]
        for key, v in d.items():
            count[v].append(key)
            
        output = []
        i = n - 1
        while i >= 0:
            
            if count[i] != 0:
                
                count[i].sort()
                
                for val in count[i]:
                    output.append(val)
                    k -= 1
                    
                    if k == 0:
                        break
            i -= 1
                        
            if k == 0:
                break
                
        return output