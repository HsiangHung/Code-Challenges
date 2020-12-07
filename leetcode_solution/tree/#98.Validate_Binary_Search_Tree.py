#  98. Validate Binary Search Tree (medium)
#  https://leetcode.com/problems/validate-binary-search-tree/
#
#  facebook, microsoft, amazon, bloomberg
#
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #
        # to make sure a BST, the mininum of right subtree should be greater than the root
        #                         maximum of left subtree should be less than the root
        #
        if not root: return True
        a, b = self.DFS(root)
        if a is False or b is False: return False
        return True
    
    
    def DFS(self, root):
        if not root.left and not root.right: 
            return root.val, root.val  
        
        min_left, max_right = root.val, root.val
        if root.left:
            min_left, max_left = self.DFS(root.left)
            if max_left is False or root.val <= max_left: return False, False
            
        if root.right:
            min_right, max_right = self.DFS(root.right)
            if max_right is False or root.val >= min_right: return False, False
        
        return min_left, max_right