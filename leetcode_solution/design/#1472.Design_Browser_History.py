#  1472. Design Browser History (medium)
#  https://leetcode.com/problems/design-browser-history/
#
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        
        nextNode = Node(url)
        self.node.next = nextNode
        nextNode.prev = self.node
        
        self.node = nextNode
    

    def back(self, steps: int) -> str:
        while steps > 0 and self.node.prev:
            self.node = self.node.prev
            steps -= 1
            
        return self.node.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.node.next:
            self.node = self.node.next
            steps -= 1
            
        return self.node.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)