## [Leetcode#563] Binary Tree Tilt
#
#
#
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_tilt(root)[1]

    def get_tilt(self, root):
        
        if not root: return 0, 0
        
        left_sum, left_tilt = self.get_tilt(root.left)
        right_sum, right_tilt = self.get_tilt(root.right)
        
        return left_sum + right_sum + root.val, left_tilt + right_tilt + abs(left_sum-right_sum)