# [# 872] Leaf-Similar Trees
#  
#
#
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: return True        
        if not root1 or not root2: return False
        return self.trasverse(root1) == self.trasverse(root2)
        
    def trasverse(self, root):
        if not root.left and not root.right: 
            return [root.val]
        
        sequence = []
        
        if root.left:
            sequence += self.trasverse(root.left)
            
        if root.right:
            sequence += self.trasverse(root.right)
            
        return sequence
                
        