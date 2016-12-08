
# Data structure: Stacks and Queues

## Stack (First-in-last-out):
```Python
class stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, x):
        self.items.append(x)
        
    def pop(self):
        self.items.pop()
        
    def get(self):
        if self.items == []: return None
        return self.items[len(self.items)-1]
```




## Queue (First-in-first-out):
```Python
class queue():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,x):
        self.items.insert(0,x)
        
    def pop(self):
        self.items.pop()
        
    def peek(self):
        if self.items == []: return None
        return self.items[len(self.items)-1]
```