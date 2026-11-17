class PrefixTree:

    def __init__(self):
        self.root = {}
       
        

    def insert(self, word: str) -> None:
        curr = self.root 
        for char in word:
            if char not in curr:
                curr[char] = {"end": False}
            curr = curr[char]
        curr["end"] = True 
      


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if curr["end"]:
            return True 
        return False 
        
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True 
      






        
        