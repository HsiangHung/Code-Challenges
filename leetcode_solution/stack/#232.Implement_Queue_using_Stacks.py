#  232. Implement Queue using Stacks (easy)
#  https://leetcode.com/problems/implement-queue-using-stacks/
#  
#  The idea is to implement two stacks to form a queue
#
#     [..   ...]  is a stack
#    front    back 
#
#  action         stack1   stack2
#  push 1,2,3    [1,2,3]   [] 
#  pop           []        [3,2,1]  =>  []   [3,2]
#  push 4        [4]       [3,2]
#  push 5        [4,5]     [3,2]
#  pop           [4,5]     [3]
#  pop           [4,5]     []
#  pop           []        [5,4]    =>  []   [5]
#
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        else:
            if self.stack2.size() > 0:
                return self.stack2.pop()
            else:
                while self.stack1.size() > 0:
                    x = self.stack1.pop()
                    self.stack2.push(x)
        
                return self.stack2.pop()            
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None
        else:
            if self.stack2.size() > 0:
                return self.stack2.peek()
            else:
                while self.stack1.size() > 0:
                    x = self.stack1.pop()
                    self.stack2.push(x)
        
                return self.stack2.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1.size() == self.stack2.size() == 0
        
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()