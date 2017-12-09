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
        if not p and not q: return True
        if not p or not q: return False
        
        if p.val != q.val: return False
        
        if not p.left and not p.right and not q.left and not q.right: return True
        
        isSame = True
        
        if p.left and q.left:
            isSame = isSame and self.isSameTree(p.left, q.left)
        elif p.left or q.left:
            return False
        
        if p.right and q.right:
            isSame = isSame and self.isSameTree(p.right, q.right)
        elif p.right or q.right:
            return False
            
        return isSame
            
            
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