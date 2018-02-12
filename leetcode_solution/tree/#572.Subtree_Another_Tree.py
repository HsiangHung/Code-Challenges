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
        
        if s and t:
            if s.val == t.val:
                
                # if s =t, start to compare. Even False, still continue search until end of s tree
                if self.isSameTree(s, t):
                    return True
    
            if s.left and s.right:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            elif s.left and not s.right:
                return self.isSubtree(s.left, t)
            elif not s.left and s.right:
                return self.isSubtree(s.right, t)
            else:
                return False
        else:
            return False
        
        

        
    def isSameTree(self, s, t):
        if s and t:
            if s.val != t.val: return False
            
            if s.left and t.left and s.right and t.right:
                return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
            elif s.left and t.left and not s.right and not t.right:
                return self.isSameTree(s.left, t.left)
            elif not s.left and not t.left and s.right and t.right:
                return self.isSameTree(s.right, t.right)
            elif not s.left and not t.left and not s.right and not t.right:
                return True
            else:
                return False
        elif not s and not t:
            return True
        else:
            return False