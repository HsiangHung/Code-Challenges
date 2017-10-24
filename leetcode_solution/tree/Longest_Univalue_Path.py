## [Leetcode#687] Longest Univalue Path
##
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        return self.traverse(root)[1]
        
        
    def traverse(self, root):
        if not root.left and not root.right: return 0, 0

        left_path, max_left_path = 0, 0
        if root.left:
            left_path, max_left_path = self.traverse(root.left)
            if root.val == root.left.val: 
                left_path += 1
            else:
                left_path = 0

        right_path, max_right_path = 0, 0
        if root.right:
            right_path, max_right_path = self.traverse(root.right)
            if root.val == root.right.val: 
                right_path += 1
            else:
                right_path = 0
        
        return max(left_path, right_path), max(left_path+right_path, max_left_path, max_right_path)