# [#617] Merge Two Binary Trees
#
#
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        if not t1: return t2
        
        if t1 and t2:
            t1.val += t2.val
            if t1.left:
                self.mergeTrees(t1.left, t2.left)
            elif not t1.left and t2.left:
                t1.left = t2.left
                
            if t1.right:
                self.mergeTrees(t1.right, t2.right)
            elif not t1.right and t2.right:
                t1.right = t2.right
                
        elif t1:
            self.mergeTrees(t1.left, None)
            self.mergeTrees(t1.right, None)
        
        return t1