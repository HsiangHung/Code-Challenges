## Q4.4 generate linked lists for each layer
## idea: using preorder traverse.
##       We always fit the head of a linked list on each layer first, and 
##       later traversal to next node
##
class treeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

def create_linkedLists(tree, heads, linkList, depth):
    if tree != None:
        print(tree.val, depth)
        if depth not in heads:
            linkList[depth] = Node(tree.val)
            heads[depth] = linkList[depth]
        else:
            linkList[depth].next = Node(tree.val)
            linkList[depth] = linkList[depth].next
            
        find_depth(tree.left, heads, linkList, depth+1)
        find_depth(tree.right, heads, linkList, depth+1)



## ----------------
## test function

## creating a  tree:
A = treeNode(0)
B = treeNode(1)
C = treeNode(2)
D = treeNode(3)
E = treeNode(4)
F = treeNode(5)
G = treeNode(6)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

H = treeNode(7)
I = treeNode(8)
J = treeNode(9)
K = treeNode(10)
E.left = H
E.right = I
F.right = J
G.left = K


heads = {}
linkList ={}
create_linkedLists(A, heads, linkList, 0)


print ('linked lists:')
#print (heads)

for depth in heads:
    node = heads[depth]
    print (node.val)
    while node.next != None:
        node = node.next
        print (node.val)
    print ('------')