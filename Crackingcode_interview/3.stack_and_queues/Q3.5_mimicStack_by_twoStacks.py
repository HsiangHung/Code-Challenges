## Q3.5: use two stacks to implement a queue
#
#  idea: using two stacks to pop can mimic a queue
#
class MyQueue():
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.append(x)
        
    def pop(self):
        C = stack()
        for i in range(len(self.items)-1,0,-1):
            C.push(self.items[i])
            
        #print (C.get())
            
        self.items = []
        while C.get() != None:
            #print (C.get(), type(C.get()))
            self.items.append(C.get())
            C.pop()
            #print (C.get())

    def get(self):
        if self.items == []: return None
        return self.items[0]

A = MyQueue()
A.push(5)
A.push(10)
A.push(1)
A.push(20)      

print (A.get())

A.pop()
print (A.get())
A.pop()
print (A.get())
A.pop()
print (A.get())
A.pop()
print (A.get())