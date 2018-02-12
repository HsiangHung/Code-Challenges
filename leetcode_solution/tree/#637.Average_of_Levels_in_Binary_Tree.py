#[Leetcode#637] Average of Levels in Binary Tree
#
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        
        avg_level = {}
        self.traverse(avg_level, root, 0)
        
        avg_level = {x: float(sum(avg_level[x]))/len(avg_level[x]) for x in avg_level}
        return [x[1] for x in sorted(avg_level.items())]
        
    def traverse(self, avg_level, root, depth):
        
        if depth not in avg_level:
            avg_level[depth] = [root.val]
        else:
            avg_level[depth].append(root.val) 
        
        if not root.left and not root.right:
            return 
        
        if root.left:
            self.traverse(avg_level, root.left, depth+1)
            
        if root.right:
            self.traverse(avg_level, root.right, depth+1)