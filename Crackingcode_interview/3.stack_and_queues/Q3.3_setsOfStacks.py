## Q3.3: sets of stacks with finite capacity on each stack
#
class Set0fStacks():
    def __init__(self, c):
        self.items = []
        self.capacity = c
        
    def push(self, x):
        lastStack = len(self.items)-1
        if lastStack == -1:
            ## start to [[]]
            self.items.append([x])
            return
        
        if len(self.items[lastStack]) < self.capacity:
            ## direct push
            self.items[lastStack].append(x)
        else:
            ## if the stack is full, create another new stack
            self.items.append([x])
            
    def pop(self):
        lastStack = len(self.items)-1
        if len(self.items[lastStack]) == 1:
            ## e.g. [[1,2,3],[4]] -> [[1,2,3]]
            self.items.pop()
        else:
            ## e.g. [[1,2,3],[4,5]] -> [[1,2,3],[4]]
            self.items[len(self.items)-1].pop()
            
    def popAt(self, x):
        self.items.remove(self.items[x])
        
    def show(self):
        print (self.items)

A = Set0fStacks(3)
A.push(0)
A.push(1)
A.push(2)
A.push(3)
A.push(4)
A.push(5)
A.push(6)
#A.show()
#A.pop()
#A.show()
#A.pop()
#A.show()
A.popAt(1)
A.show()
