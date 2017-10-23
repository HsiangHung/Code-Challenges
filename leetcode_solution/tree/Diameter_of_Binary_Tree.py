## [Leetcode#543] Diameter of Binary Tree
##
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        return self.traverse(root)[1]
    
    
    def traverse(self, root):
        if not root.left and not root.right: return 0, 0
        
        left_dist, right_dist = 0, 0
        max_left_dist, max_right_dist = 0, 0
        if root.left:
            left_dist, max_left_dist = self.traverse(root.left)
            left_dist += 1
        
        if root.right:
            right_dist, max_right_dist = self.traverse(root.right)
            right_dist += 1
            
        return max(left_dist, right_dist), max(max_left_dist, max_right_dist, left_dist + right_dist)