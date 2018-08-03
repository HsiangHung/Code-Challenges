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
        self.leaves = {1: [], 2: []}
        self.traversal(root1, 1)
        self.traversal(root2, 2)
        return self.leaves[1] == self.leaves[2]
        
        
    def traversal(self, root, tree):
        if not root.left and not root.right:
            self.leaves[tree].append(root.val)
            return

        if root.left:
            self.traversal(root.left, tree)
            
        if root.right:
            self.traversal(root.right, tree)
                
        