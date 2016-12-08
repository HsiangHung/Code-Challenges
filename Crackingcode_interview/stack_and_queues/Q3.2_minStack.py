## Q3.2: design a MinStack, which push, pop and min are all O(1) complexity.
#
class minStack():
    def __init__(self):
        self.reg = []
        self.min = []
        
    def push(self,x):
        self.reg.append(x)
        if self.min == []:
            self.min.append(x)
        else:
            if x < self.min[len(self.min)-1]:
                self.min.append(x)
                
    def pop(self):
        last = self.reg[len(self.reg)-1]
        if last == self.min[len(self.min)-1]:
            self.min.pop()
        self.reg.pop()
        
    def get_min(self):
        return self.min[len(self.min)-1]
    
    
A = minStack()
A.push(1)
A.push(5)
print (A.get_min())

A.push(100)
print (A.get_min())

A.push(-5)
A.pop()
print (A.get_min())