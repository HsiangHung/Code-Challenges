## [Leetcode#572] Subtree of Another Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t: return True
        if not s or not t: return False
        
        if s.val == t.val:
            if self.isSameTree(s, t):
                return True
            
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)