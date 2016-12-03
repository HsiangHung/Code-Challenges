
# Datastructure: Tree 

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

# in-order (Making Bindary seach tree)
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

# Easy level




## Q3: Lowest Common Ancestor of a Binary Search Tree
### Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
```Python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        if p.val > q.val:
            return self.getNode(root, q, p)
        else:
            return self.getNode(root, p, q)
        
    def getNode(self, root, p, q):
        """
        : type root, p, q: TreeNode (q > p)
        " rtype: int
        """
        if p.val <= root.val <= q.val: return root.val
        
        if p.val <= root.val and q.val <= root.val:
            return self.getNode(root.left, p, q)
            
        if p.val >= root.val and q.val >= root.val:
            return self.getNode(root.right, p, q)
```
The following considers even not a BST, it still wors since it stores all path and it's ancestors.
```Python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.path = {}
        self.traverse(root, str(root.val))
        a1 = self.path[p.val]
        a2 = self.path[q.val].split(',')
        for ans1 in a1.split(','):
            if ans1 in a2: return int(ans1)
            
    def traverse(self, node, path):
        self.path[node.val] = path
        if node.left == None and node.right == None: return
            
        if node.left != None:
            self.traverse(node.left, str(node.left.val)+','+path)
                
        if node.right != None:
            self.traverse(node.right, str(node.right.val)+','+path)
```
but the followings:
```Python
    def lowestCommonAncestor(self, root, p, q):
        self.path = {}
        self.wrongTraverse(root, [root.val])
        a1 = self.path[p.val]
        a2 = self.path[q.val]
        for ans1 in a1:
            if ans1 in a2: return int(ans1)
            
     def wrongTraverse(self, node, path):
        if node.left == None and node.right == None:
            self.path[node.val] = path
            return
            
        if node.left != None:
            self.path[node.val] = path
            self.wrongTraverse(node.left, path.append(node.left.val))
                
        if node.right != None:
            self.path[node.val] = path
            self.wrongTraverse(node.right, path.append(node.right.val))
```
and
```Python
    def wrongTraverse2(self, node, path):
        if node.left == None and node.right == None:
            self.path[node.val] = path
            return
            
        if node.left != None:
            self.path[node.val] = path
            path.append(node.left.val)
            self.wrongTraverse2(node.left, path)
                
        if node.right != None:
            self.path[node.val] = path
            path.append(node.right.val)
            self.wrongTraverse2(node.right, path)
```
don't work. The first one, passing ```list.append(x)``` will give ```None```, so
it won't give anything. (One can check ```print [5].append(6)``` gives ```None```).
The second one is to append ```x``` before passing ```path``` in recursion. But doing this
will append all nodes in the ```path``` list; won't generate each list for each path.


## Q5: Invert Binary Tree
```Python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return root
        self.traverse(root)
        return root
        
    def traverse(self, root):
        if root.left == None and root.right == None: return
    
        if root.left != None and root.right != None:
            Left = root.left
            self.traverse(Left)
            Right = root.right
            self.traverse(Right)
            root.right = Left
            root.left = Right
        elif root.left != None and root.right == None:
            self.traverse(root.left)
            root.right = root.left
            root.left = None
        elif root.left == None and root.right != None:
            self.traverse(root.right)
            root.left = root.right
            root.right = None
```

## Q6: Same Tree
### Given two binary trees, write a function to check if they are equal or not.
```Python
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None: return True
        if p == None or q == None: return False
        return self.traverse(p,q)
        
    def traverse(self, p, q):
        if p.val != q.val: return False
        if p.left == None and p.right == None and q.left == None and q.right == None: return True

        if p.left != None and q.left != None and p.right != None and q.right != None:
            return self.traverse(p.left, q.left) and self.traverse(p.right, q.right)
        elif p.left != None and q.left != None and p.right == None and q.right == None:
            return self.traverse(p.left, q.left)
        elif p.left == None and q.left == None and  p.right != None and q.right != None:
            return self.traverse(p.right, q.right)
        else:    
            return False
```

## Q7: Symmetric Tree
### Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). For example, the binary tree ```[1,2,2,3,4,4,3]``` is symmetric, but ```[1,2,2,null,3,null,3]``` is not.
```Python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        if root.left == None and root.right == None: return True
        if root.left != None and root.right != None:
            return self.traverse(root.left, root.right)
        else:
            return False
        
    def traverse(self, left, right):
        if left.val != right.val: return False
        
        if left.left == None and left.right == None and right.left == None and right.right == None: return True
        
        if left.left != None and right.right != None and left.right != None and right.left != None:
            return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)
        elif left.left != None and right.right != None and left.right == None and right.left == None:
            return self.traverse(left.left, right.right)
        elif left.left == None and right.right == None and left.right != None and right.left != None:
            return self.traverse(left.right, right.left)
            
        return False
```

## Q8: Minimum Depth of Binary Tree
### Given a binary tree, find its minimum depth.
```Python
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.min = float('inf')
        self.traverse(root, 1)
        return self.min
        
    def traverse (self, root, depth):
        if root.left == None and root.right == None: 
            self.min = min(self.min, depth)
            return
    
        if root.left != None: self.traverse(root.left, depth+1)
        
        if root.right != None: self.traverse(root.right, depth+1)
```

## Q9: Balanced Binary Tree
### Given a binary tree, determine if it is height-balanced.
```Python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        self.isBalanced = True
        self.traverse(root)
        return self.isBalanced
        
    def traverse(self, root):
        if root.left == None and root.right == None: return 0
        Ldepth = 0
        Rdepth = 0
        
        if root.left != None: Ldepth = self.traverse(root.left)+1
            
        if root.right != None: Rdepth = self.traverse(root.right)+1
            
        if abs(Ldepth-Rdepth) >1: self.isBalanced = False
 
        return max(Ldepth, Rdepth)
```
other solution format (thank to Emmanuel)
```Python
        h = self.getHeight(root)+1
        if h == -1: return False
        return True
        #return abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 

    def getHeight(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if root.left == None and root.right == None: return 0

        if root.left != None and root.right != None:
            h_L = self.getHeight(root.left)+1
            h_R = self.getHeight(root.right)+1
        elif root.left != None and root.right == None: 
            h_L = self.getHeight(root.left)+1
            h_R = 0
        elif root.left == None and root.right != None:
            h_L = 0
            h_R = self.getHeight(root.right)+1
        
        if h_L == -1 or h_R == -1: return -2
            
        diff = abs(h_L-h_R)
        if diff <= 1: 
            return max(h_L, h_R)
        else:
            return -2
```

## Q10: Sum of Left Leaves
### Find the sum of all left leaves in a given binary tree.
```Python
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.leftSum = 0
        self.isLeaf(root)
        return self.leftSum
        
    def isLeaf(self, root):
        if root.left == None and root.right == None: return True
    
        if root.left != None:
            if self.isLeaf(root.left) == True: self.leftSum += root.left.val
            
        if root.right != None: self.isLeaf(root.right)
            
        return False
```

## Q11: Closest Binary Search Tree Value
### Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
```Python
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closetNode = float('inf')
        self.traverse(root, target)
        return self.closetNode
        
    def traverse(self, node, target):
        print node.val
        
        if float(node.val) == target:
            self.closetNode = node.val
            return
        
        if abs(self.closetNode-target) > abs(node.val-target): self.closetNode = node.val
        
        if node.left == None and node.right == None: return
    
        if node.val > target and node.left != None: self.traverse(node.left, target)
        
        if node.val < target and node.right != None: self.traverse(node.right, target)
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

## Q3: [Leetcode#199] Binary Tree Right Side View
### Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
```Python
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sideView = []
        if root == None: return []
        
        self.traverse(root,1)
        return self.sideView
        
    def traverse(self, root, depth):
        if len(self.sideView) < depth: self.sideView.append(root.val)
        if root.right == None and root.left == None: return
    
        if root.right != None: self.traverse(root.right, depth+1)
        if root.left != None: self.traverse(root.left, depth+1)
```


## Q4: [Leetcode#98] Validate Binary Search Tree
### Given a binary tree, determine if it is a valid binary search tree (BST).

solution 1: perform in-order traversal, and if the current root < previous, it is False
```Python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        self.stack = []
        self.isValidBST = True
        self.traverse(root)
        return self.isValidBST
        
        
    def traverse(self, root):
        if root.left == None and root.right == None: 
            #print root.val
            if len(self.stack) != 0: 
                if root.val <= self.stack[len(self.stack)-1]: 
                    self.isValidBST = False
                else:
                    self.stack.pop()
                    self.stack.append(root.val)
                return
            else:
                self.stack.append(root.val)
                return
        
        if root.left != None:
            self.traverse(root.left)
            
        #print root.val
        
        if len(self.stack) != 0:
            if root.val <= self.stack[len(self.stack)-1]:
                self.isValidBST = False
                return
            else:
                self.stack.pop()
                self.stack.append(root.val)
        else:
            self.stack.append(root.val)

        if root.right != None:
            self.traverse(root.right)
```
solution 2: check if always max(left subtree) < root < min(right subtree)
```Python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        if root.left == None and root.right == None: return True
        
        max_node, min_node = self.getVal(root)
        
        if max_node == 'False' and 'min_node' == False: return False
        
        if max_node!= None and min_node!=None: return min_node <= root.val <= max_node
        if max_node!='False' and min_node =='False': return root.val <= max_node
        if max_node== 'False' and min_node!='False': return min_node <= root.val
        
        return False

    
    def getVal(self, root):
        
        if root.left == None and root.right == None: return root.val, root.val
        
        max_L = None
        if root.left != None:
            max_L, min_L = self.getVal(root.left)
            if max_L == 'False' or min_L=='False': return 'False', 'False'
            
        min_R = None
        if root.right != None:
            max_R, min_R = self.getVal(root.right)
            if max_R=='False' or min_R=='False': return 'False', 'False'
    
        if max_L != None and min_R != None:
            if max_L < root.val < min_R: return max_R, min_L
        elif max_L != None and min_R == None:
            if max_L < root.val: return root.val, min_L
        elif max_L == None and min_R != None:
            if root.val < min_R: return max_R, root.val
        
        return 'False', 'False'
```
