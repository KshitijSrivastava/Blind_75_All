
# 50 Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        visited = set()
        d = {}
        
        queue = []
        queue.append( node )
        visited.add( node )
        
        d[node] = Node(node.val)
        
        while queue:
            
            n = queue.pop(0)
            #Loop through all the neightbours of the Node
            for n_n in n.neighbors:
                #if neighbouring node not in dict, then make the node
                if n_n not in d:
                    d[n_n] = Node( n_n.val )
                
                #append the cloned neighbouring node the the neighbouring
                d[n].neighbors.append( d[n_n] )
                
                if n_n not in visited:
                    visited.add(n_n)
                    queue.append(n_n)
                    
        return d[node]

