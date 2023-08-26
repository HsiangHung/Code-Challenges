
# Data structure: Linked lists

```Python
class LinkNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
def printList(head):
    node = head
    while node.next != None:
        print(node.val)
        node = node.next
    print(node.val)        
```
test
```Python
A = LinkNode(3)
B = LinkNode(2)
C = LinkNode(6)
D = LinkNode(9)
E = LinkNode(2)
F = LinkNode(10)
G = LinkNode(9)
H = LinkNode(100)
 
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H

## check the list
printList(A)
```

