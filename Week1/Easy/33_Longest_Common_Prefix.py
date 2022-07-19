
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_length = min( [ len(s) for s in strs] )
        
        result = []
        
        for i in range(min_length):
            
            for j in range( len(strs) ):
                if strs[j][i] != strs[0][i]:
                    return "".join(result)
                
            result.append( strs[0][i] )
            
        return "".join(result)
