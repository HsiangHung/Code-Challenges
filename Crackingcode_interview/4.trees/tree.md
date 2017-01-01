
# Data structure: Tree 

### The tree class in Leetcode is defined as
```Python
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
```

## setup a tree:
```Python
A = TreeNode(10)
B = TreeNode(5)
C = TreeNode(15)
D = TreeNode(1)
E = TreeNode(6)
F = TreeNode(12)
G = TreeNode(20)
H = TreeNode(2)
I = TreeNode(8)
J = TreeNode(11)
K = TreeNode(13)
L = TreeNode(18)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.right = H
E.right = I
F.left = J
F.right = K
G.left = L
```



# Pre-order
input `[10,5,15,1,6,12,20,null,2,null,8,11,13,18]`
```Python
def preOrder(root):
    print (root.val)
    if root.left == None and root.right == None: return        
    if root.left != None: preOrder(root.left)
    if root.right != None: preOrder(root.right)
preOrder(A)
```
gives
```
10
5
1
2
6
8
15
12
11
13
20
18
```

# in-order (judging binary search tree)
input `[10,5,15,1,6,12,20,null,2,null,8,11,13,18]`
```Python
def inOrder(root):
    if root.left == None and root.right == None: 
        print (root.val)
        return
        
    if root.left != None: inOrder(root.left)
    print (root.val)
    if root.right != None: inOrder(root.right)
inOrder(A)
```
gives 
```
1
2
5
6
8
10
11
12
13
15
18
20
```

# Post-order 
```Python
def postOrder(root):
    if root.left == None and root.right == None: 
        print (root.val)
        return
    if root.left != None: postOrder(root.left)
    if root.right != None: postOrder(root.right)
    print (root.val)
postOrder(A)
```
gives 
```
2
1
8
6
5
11
13
12
18
20
15
10
```
Another ways to represent preorder, inorder and postorder:
```Python
def preorder(root):
    if root != None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```



# BFS on tree
```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def BreadthFirstSearch(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.getHeight(root)
        #print h
        for i in range(1, h+1):
            self.printLevel(root, i)
            
    def printLevel(self, root, level):
        if level ==0:
            return
        elif level == 1:
            print root.val
        elif level > 1:
            if root.left != None: self.printLevel(root.left, level-1)
            if root.right != None: self.printLevel(root.right, level-1)
        
    def getHeight(self, root):
        if not root.left and not root.right: return 1
        h_L = 0
        if root.left != None: h_L = self.getHeight(root.left)+1
        h_R = 0
        if root.right != None: h_R = self.getHeight(root.right)+1
        return max(h_L, h_R)
```








