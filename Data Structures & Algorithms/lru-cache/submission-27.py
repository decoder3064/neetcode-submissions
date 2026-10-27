class Node: 
    def __init__(self, key: int = 0, val: int = 0,
                prev: Node = None, next: Node = None):

        self.key = key
        self.val = val
        self.next = next 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.memo = {}
        self.head = None 
        self.back = None 

    def get(self, key: int) -> int:

        if key  not in self.memo:
            return -1

        node = self.memo[key]

        if node == self.head:
            return node.val

        if self.memo[key] == self.back and self.size > 1: 
            self.back = self.back.next 

        
        prev_tp = node.prev
        next_tp = node.next 

        if prev_tp and prev_tp.next: 
            prev_tp.next = next_tp

        if next_tp:
            next_tp.prev = prev_tp

        node.prev = self.head 
        self.head.next = node 
        self.head = node
        
            
            
        return self.memo[key].val  


        


    def put(self, key: int, value: int) -> None:
        
        new_node = Node(key,value ,self.head)
        
        if key in self.memo:
            self.memo[key].val = value
            self.get(key)
            return

       

        if self.size  < 1: 
            self.back = new_node 
        else: 
            self.head.next = new_node 
        
        self.head = new_node 
        self.memo[key] = new_node

        self.size +=1

        if self.size > self.capacity: 
            temp = self.back.next 
            self.back.next = None 
            if temp:
                temp.prev = None 
            self.memo.pop(self.back.key)
            self.back = temp 
            self.size-=1 

       

        


            

        




      
        
