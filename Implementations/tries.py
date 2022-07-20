class Node:
    def __init__(self):
        self.child = {}
        self.isEnd = False
        
        
class Trie:

    def __init__(self):
        self.root = Node()

    
    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if not char in curr.child:
                curr.child[char] = Node()
                
            curr = curr.child[char]
            
        curr.isEnd = True
        
        
    
    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if not char in curr.child:
                return False
            
            curr = curr.child[char]
        
        return curr.isEnd

    
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if not char in curr.child:
                return False
            
            curr = curr.child[char]
        
        return True
