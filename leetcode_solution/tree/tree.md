
# Data structure: Tree 

### The tree class in Leetcode is defined as
```Python
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
```
# Pre-order
input `[10,5,15,1,6,12,20,null,2,null,8,11,13,18]`
```Python
    def preOrder(self, root):
        print root.val
        if root.left == None and root.right == None: return
        
        if root.left != None: self.preOrder(root.left)
        
        if root.right != None: self.preOrder(root.right)
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
    def inOrder(self, root):
        if root.left == None and root.right == None: 
            print root.val
            return
        
        if root.left != None: self.inOrder(root.left)
            
        print root.val
        
        if root.right != None: self.inOrder(root.right)
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
    def postOrder(self, root):
        if root.left == None and root.right == None: 
            print root.val
            return
        
        if root.left != None: self.postOrder(root.left)
        if root.right != None: self.postOrder(root.right)

        print root.val
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

Both solutions use stack. 
First one is more concise.

```Python
class Solution1(object):
    def BreadthFirstSearch(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.BFS([root], 0)
        
    def BFS(self, stack, depth):
        next_stack = []
        while len(stack) > 0:
            node = stack.pop(0)
            
            print (node.val, depth)

            if node.left:
                next_stack.append(node.left)
                
            if node.right:
                next_stack.append(node.right)

            # note, here we need to go through nodes in the same layer, then next recursion
        
        if len(next_stack) > 0:       
            self.BFS(next_stack, depth+1)
```
gives
```
10 0
5 1
15 1
1 2
6 2
12 2
20 2
2 3
8 3
11 3
13 3
18 3
```

```Python
class Solution2(object):
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











## Q12: [Leetcode#366] Find Leaves of Binary Tree
### Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
```Python
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        
        self.leavesDepth = []
        while root.left != None or root.right != None:
            self.leaves = []
            self.traverse(root)
            self.leavesDepth.append(self.leaves)
            
        self.leavesDepth.append([root.val])
        return self.leavesDepth
        
    def traverse(self, root):
        if root.left == None and root.right == None: 
            self.leaves.append(root.val)
            return 'Leaves'
        
        if root.left != None:
            if self.traverse(root.left) == 'Leaves': root.left = None
            
        if root.right != None:
            if self.traverse(root.right) == 'Leaves': root.right = None
```

# Medium level

## Q2: [Leetcode#156] Binary Tree Upside Down

### Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
```Python
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return root
        self.traverse(root)
        root.left = None
        root.right = None
        return self.root
        
    def traverse(self, root):
        '''self.root is the upside down root'''
        if root.left == None: 
            self.root = root
            return
        
        if root.left != None: self.traverse(root.left)
            
        if root.right != None:
            (root.left).left = root.right
        else:
            (root.left).left = None

        (root.left).right = root
```
`self.root` is the new root after upside down (the left leaf of the bottom layer). One can define another traverse function and call the function `self.traverse2(self.root)` in the main function to check:
```Python
    def traverse2(self, root):
        print root.val
        if root.left == None and root.right == None: return
        
        if root.left != None: self.traverse2(root.left)        
        if root.right != None: self.traverse2(root.right)
```
Input `[1,2,null, 3]` returns `[3,null,2,null,1]`. Input `[1,2, 3,4,5,null,null,6,7]` returns `[6,7,4,null,null,5,2,null,null,3,1]`.



