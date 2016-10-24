
# Datastructure: Tree 


## Q1: Binary Tree Paths
### Given a binary tree, return all root-to-leaf paths.
```
input: [5,4,8,11,null,13,6,7,2,null,null,null,1]
```
```Python
class Solution(object):
    def findAllPath(self, root):
        """
        :type root: TreeNode
        """ 
        self.traverse(root, str(root.val))

    def traverse(self, node, path):
        if node.left == None and node.right == None:
            print (path)
            return

        if node.left != None:
            self.traverse(node.left, str(node.left.val)+'->'+path)
                
        if node.right != None:
            self.traverse(node.right, str(node.right.val)+'->'+path)
```
gives
```
7->11->4->5
2->11->4->5
13->8->5
1->6->8->5
```

## Q2: Lowest Common Ancestor of a Binary Search Tree
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
        self.path = {}
        self.traverse(root, str(root.val))
        a1 = self.path[p.val]
        a2 = self.path[q.val].split(',')
        for ans1 in a1.split(','):
            if ans1 in a2: return int(ans1)
            
    def traverse(self, node, path):
        if node.left == None and node.right == None:
            self.path[node.val] = path
            return
            
        if node.left != None:
            self.path[node.val] = path
            self.traverse(node.left, str(node.left.val)+','+path)
                
        if node.right != None:
            self.path[node.val] = path
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


## Q3: Path Sum
### Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
```Python
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        
        self.sum = {}
        self.traverse(root, str(root.val), root.val)
        
        if sum in self.sum: return True
        return False

        
    def traverse(self, node, path, pathSum):
        if node.left == None and node.right == None:
            #print (path):
            self.sum[pathSum] = path
            return

        if node.left != None:
            self.traverse(node.left, str(node.left.val)+'->'+path, pathSum+node.left.val)
                
        if node.right != None:
            self.traverse(node.right, str(node.right.val)+'->'+path, pathSum+node.right.val)
```


## Q4: Invert Binary Tree
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

## Q5: Same Tree
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

## Q6: Symmetric Tree
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

## Q7: Minimum Depth of Binary Tree
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
    
        if root.left != None:
            self.traverse(root.left, depth+1)
        
        if root.right != None:
            self.traverse(root.right, depth+1)
```

## Q8: Balanced Binary Tree
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
        
        if root.left != None:
            Ldepth = self.traverse(root.left)+1
            
        if root.right != None:
            Rdepth = self.traverse(root.right)+1
            
        if abs(Ldepth-Rdepth) >1: self.isBalanced = False
 
        return max(Ldepth, Rdepth)
```
