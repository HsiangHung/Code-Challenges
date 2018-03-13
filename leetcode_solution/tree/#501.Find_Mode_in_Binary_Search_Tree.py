# [# 501] Find Mode in Binary Search Tree
# 
#
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        mode_dict = {}
        for num in self.traverse(root):
            mode_dict[num] = mode_dict.get(num, 0)+1
            
        max_freq = max([mode_dict[num] for num in mode_dict])
        return [num for num in mode_dict if mode_dict[num] == max_freq]
        
        
    def traverse(self, root):
        if not root.left and not root.right:
            return [root.val]
        
        nodes = []
        if root.left:
            nodes += self.traverse(root.left)
                
        nodes.append(root.val)
        
        if root.right:
            nodes += self.traverse(root.right)
            
        return nodes