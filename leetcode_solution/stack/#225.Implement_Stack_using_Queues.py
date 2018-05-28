## [Leetcode#225] Implement Stack using Queues
#
#  Bloomberg
#
class Queue(object):
    def __init__(self):
        self.items = []
        
    def push(self, x):
        self.items.insert(0, x)
        
    def pop(self):
        if self.empty():
            return None
        else:
            return self.items.pop()
    
    def peek(self):
        if self.empty():
            return None
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
        
    def empty(self):
        return len(self.items) == 0

#  idea: always push value to non-empty queue, when need to peek or pop
#        move all elements to the other empty until the last element
#
#  action         queue1      queue2
#  push 1,2,3     [3,2,1]     []
#  pop            [3]         [2,1]     => []   [2,1] and get 3
#  push 4         []          [4,2,1]
#  top            [4,2,1]     []        to get 4
#
#   
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.queue1.empty() and self.queue2.empty():
            self.queue1.push(x)
        elif self.queue1.empty() and not self.queue2.empty():
            self.queue2.push(x)
        elif not self.queue1.empty() and self.queue2.empty():
            self.queue1.push(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue1.empty() and self.queue2.empty():
            return None
        else:
            if self.queue1.empty():
                while self.queue2.size() > 1:
                    x = self.queue2.pop()
                    self.queue1.push(x)
                return self.queue2.pop()
            elif self.queue2.empty():
                while self.queue1.size() > 1:
                    x = self.queue1.pop()
                    self.queue2.push(x)
                return self.queue1.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        
        if self.queue1.empty() and self.queue2.empty():
            return None
        else:
            if self.queue1.empty():
                while self.queue2.size() > 0:
                    x = self.queue2.pop()
                    self.queue1.push(x)
                return x
            elif self.queue2.empty():
                while self.queue1.size() > 0:
                    x = self.queue1.pop()
                    self.queue2.push(x)
                return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue1.empty() and self.queue2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()