#[Leetcode#637] Average of Levels in Binary Tree
#
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.level_dict = {}
        self.traverse(0, root)
        return [1.0*sum(self.level_dict[level])/len(self.level_dict[level]) for level in self.level_dict]
    
    
    def traverse(self, level, root):
        if level not in self.level_dict:
            self.level_dict[level] = [root.val]
        else:
            self.level_dict[level].append(root.val)
        
        if not root.left and not root.right: return
        
        if root.left:
            self.traverse(level+1, root.left)
            
        if root.right:
            self.traverse(level+1, root.right)
        