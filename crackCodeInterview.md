
## A. Moving-Rating Query Exercise


#### Q1: Given a binary tree, print all root-to-leaf paths
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




#### Q2: Lowest Common Ancestor of a Binary Search Tree
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








