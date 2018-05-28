## [Leetcode#102] Binary Tree Level Order Traversal
##
## Facebook, Amazon, Microsoft, Bloomberg, Apple, LinkedIn
##
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        self.levels = []
        self.traversal(1, root)
        return self.levels
    
    def traversal(self, depth, root):
        if len(self.levels) < depth:
            self.levels.append([root.val])
        else:
            self.levels[depth-1].append(root.val)
            
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traversal(depth + 1, root.left)

        if root.right:
            self.traversal(depth + 1, root.right)


