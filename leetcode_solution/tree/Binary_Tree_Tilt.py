## [Leetcode#563] Binary Tree Tilt
##
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.traverse(root)[1]
    
    def traverse(self, root):
        if not root.left and not root.right: return root.val, 0

        left_sum, left_tilt = 0, 0
        if root.left:
            left_sum, left_tilt = self.traverse(root.left)
            
        right_sum, right_tilt = 0, 0
        if root.right:
            right_sum, right_tilt = self.traverse(root.right)
            
        return left_sum+right_sum+root.val, abs(left_sum - right_sum) + left_tilt + right_tilt