## Q4.6 Next method of a Tree
#
class treeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def nextGeneration(left, right):
    
    print (left.val, right.val)
    left.next = right
            
    if left.left == None and left.right == None and right.left == None and right.right == None: return
        
    if left.left != None and left.right != None:
        nextGeneration(left.left, left.right)
            
    if right.left != None and right.right != None:
        nextGeneration(right.left, right.right)
        
    if left.right != None and right.left != None:
        nextGeneration(left.right, right.left)
        
        
        
### the followings are checking functions:

def check(root):
    if root.next != None: print ('a',root.val, root.next.val)
    if root.left == None and root.right == None: return
    if root.left != None: check(root.left)
    if root.right != None: check(root.right)
    #print ('a',root.left.val, root.left.next.val)

## creating a binary tree:
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
F.left = J
F.right = K

traverse(A)

nextGeneration(A.left, A.right)
check(A)

