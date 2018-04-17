## [Leetcode#543] Diameter of Binary Tree
##
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.traversal(root))
    
    def traversal(self, root):
        if not root: return 0, 0
        
        L, R, max_L, max_R = 0, 0, 0, 0
        if root.left:
            L, max_L = self.traversal(root.left)
            L += 1
            
        if root.right:
            R, max_R = self.traversal(root.right)
            R += 1
                
        return max(L, R), max(max_L, max_R, L+R)