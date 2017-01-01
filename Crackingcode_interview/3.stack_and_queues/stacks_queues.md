
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
        
    def peek(self):
        if self.items == []: return None
        return self.items[len(self.items)-1]
```
test:
```Python
A = stack()
print (A.isEmpty())
A.push(10)
A.push(5)
print (A.peek())

A.pop()
A.push(100)
print (A.peek())
print (A.isEmpty())
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
test
```Python
A = queue()
print (A.isEmpty())
A.push(10)
A.push(5)
print (A.get())

A.pop()
A.push(100)
print (A.get())
print (A.isEmpty())
```

