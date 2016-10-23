
## A. Moving-Rating Query Exercise


#### Q1: Given a binary tree, print all root-to-leaf paths
```PYTHON
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #self.ancensters = {}
        self.path = {}
        self.traverse(root, str(root.val))
        #print self.path
        #print self.ancensters
        return
        
        a1 = self.path[7]
        a2 = self.path[4]#.split('->')
        #print a2
        for ans1 in a1:#.split('->'):
            #print ans1
            if ans1 in a2: break
            
        print ans1
        
        
    def traverse(self, node, path):
        if node.left == None and node.right == None:
            print (path)
            return

        if node.left != None:
            #self.path[node.val] = path
            self.traverse(node.left, str(node.left.val)+'->'+path)
                
        if node.right != None:
            #self.path[node.val] = path
            self.traverse(node.right, str(node.right.val)+'->'+path)

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










