
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    
    def __init__(self):
        self.arr = [None for i in range(26)]
        self.end = False
        
    def get_index(self, char):
        return ord(char) - ord('a')
    
    def charIsNone(self, char):
        return self.arr[ self.get_index(char) ] == None
    
    def getcharNode(self, char):
        return self.arr[ self.get_index(char) ]
    
    def setcharNone(self, char, node):
        self.arr[ self.get_index(char) ] = node
    
    def set_end(self):
        self.end = True
        
    def get_end(self):
        return self.end
    
    
class Trie:
    
    def __init__(self):
        self.root = Node()

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        
        node = self.root
        
        for char in word:
            
            if node.charIsNone(char):
                node.setcharNone(char, Node() )
            node = node.getcharNode(char)
        
        node.set_end()

    def search(self, word: str) -> bool:
        n = len(word)
        
        node = self.root
        
        queue = []
        queue.append( (node, 0) )
        
        while queue:
            
            node, idx = queue.pop(0)
            
            if idx == n and node.get_end():
                return True
            elif idx == n:
                continue
                
            elif word[idx] == ".":
                for char_node in node.arr:
                    if char_node is not None:
                        queue.append( (char_node, idx + 1) )
                        
            elif node.charIsNone(word[idx]):
                continue
            else:
                node = node.getcharNode( word[idx] )
                queue.append( (node, idx + 1) )
                
        return False