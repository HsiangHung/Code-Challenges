#  617. Merge Two Binary Trees (easy)
#  https://leetcode.com/problems/merge-two-binary-trees/  
#
#  amazon
#
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2: return
        
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        elif root1:
            return root1
        elif root2:
            return root2
                
       