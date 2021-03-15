#  716. Max Stack (easy)
#  https://leetcode.com/problems/max-stack/
#
class MaxStack:
    '''
    https://www.cnblogs.com/grandyang/p/7823424.html
    
    NOTE: the key is at PopMax(), need a tmp to remove s1 until s1[-1] == maxStack[-1] and remove
          when putting back, need to push, which also updates maxStack
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.maxStack.append(x)
        else:
            if len(self.maxStack) > 0 and x >= self.maxStack[-1]:
                self.maxStack.append(x)
            self.stack.append(x)
        
    def pop(self) -> int:
        x = self.stack.pop()
        if self.maxStack[-1] == x:
            self.maxStack.pop()
        return x
            
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]
        
    def popMax(self) -> int:
        x = self.maxStack.pop()
        tmp = []
        while len(self.stack) > 0 and self.stack[-1] != x:
            y = self.stack.pop()
            tmp.append(y)

        self.stack.pop()
        
        while len(tmp) > 0:
            y = tmp.pop()
            self.push(y)
        
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()