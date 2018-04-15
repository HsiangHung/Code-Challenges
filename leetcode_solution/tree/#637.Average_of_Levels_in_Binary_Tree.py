#[Leetcode#637] Average of Levels in Binary Tree
#
#  Facebook
#
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.level_avg = {}
        self.traversal(0, root)
        return [sum(self.level_avg[depth])*1.0/len(self.level_avg[depth]) for depth in self.level_avg]
    
    
    def traversal(self, depth, root):
        self.level_avg[depth] = self.level_avg.get(depth, []) + [root.val]
        
        if not root.left and not root.right: return
    
        if root.left:
            self.traversal(depth+1, root.left)
            
        if root.right:
            self.traversal(depth+1, root.right)