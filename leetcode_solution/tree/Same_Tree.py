## [Leetcode#100] Same Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q== None: return True
        if p == None or q== None: return False
        return self.traverse(p,q)
        
    def traverse(self, p, q):
        if p.val != q.val: return False
        
        if not p.left and not p.right and not q.right and not q.left: return True
        
        if p.left != None and q.left != None and p.right != None and q.right != None:
            return self.traverse(p.left, q.left) and self.traverse(p.right, q.right)
        elif p.left != None and q.left != None and p.right == None and q.right == None:
            return self.traverse(p.left, q.left)
        elif p.left == None and q.left == None and p.right != None and q.right != None:
            return self.traverse(p.right, q.right)
        else:
            return False
            
            
##### ----------------------------------------------------------
## more concise code:
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.checking(root.left, root.right)
        
        
    def checking(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val: return False
        return self.checking(left.left, right.right) and self.checking(left.right, right.left)