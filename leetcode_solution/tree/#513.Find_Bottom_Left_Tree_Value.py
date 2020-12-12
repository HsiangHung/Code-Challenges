#  513. Find Bottom Left Tree Value (medium)
#  https://leetcode.com/problems/find-bottom-left-tree-value/
#
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return root
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            if node.right: queue.append(node.right) 
            if node.left: queue.append(node.left)
                
        return node.val