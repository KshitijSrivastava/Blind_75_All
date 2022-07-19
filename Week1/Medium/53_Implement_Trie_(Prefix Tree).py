 #https://leetcode.com/problems/implement-trie-prefix-tree/


 class Node:
    
    def __init__(self):
        
        self.arr = [None for i in range(26)]
        self.end = False
        
    def find_index(self, char):
        return ord(char) - ord('a')
    
    def isNone_at_index(self, char):
        index = self.find_index(char)
        return self.arr[index] == None
        
    def get_node_at_index(self, char):
        index = self.find_index(char)
        return self.arr[index]
    
    def insert_node_at_index(self, char, node):
        index = self.find_index(char)
        self.arr[index] = node
        
        
    def get_end(self):
        return self.end
    
    def set_end(self):
        self.end = True
        

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        
        node = self.root
        for char in word:
            
            if node.isNone_at_index(char):
                new_node = Node()
                node.insert_node_at_index(char, new_node)
            node = node.get_node_at_index(char)
            
        node.set_end()
        

    def search(self, word: str) -> bool:
        
        node = self.root
        for char in word:
            
            if node.isNone_at_index(char):
                return False
            node = node.get_node_at_index(char)
            
        return node.get_end()
        

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for char in prefix:
            
            if node.isNone_at_index(char):
                return False
            node = node.get_node_at_index(char)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)