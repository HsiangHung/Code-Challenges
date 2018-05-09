## [Leetcode#155] Min Stack
##
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack == []:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            if self.stack[-1] == self.min_stack[-1]:
                self.stack.pop()
                self.min_stack.pop()
            else:
                self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0: return None
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()