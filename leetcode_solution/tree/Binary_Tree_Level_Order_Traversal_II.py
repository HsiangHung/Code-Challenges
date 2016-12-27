## [Leetcode#107] Binary Tree Level Order Traversal II
##
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        self.levels = {}
        max_depth = self.getDepth(root, 0)
        
        levels = []
        depth = max_depth
        while depth >= 0:
            levels.append(self.levels[depth])
            depth -= 1
        return levels        

    def getDepth(self, root, depth):
        """
        : type root: TreeNode
        "rtype int
        """
        if depth not in self.levels:
            self.levels[depth] = [root.val]
        else:
            self.levels[depth].append(root.val)
            
        if not root.left and not root.right: return depth
        
        if root.left != None and root.right != None: 
            return max(self.getDepth(root.left, depth+1), self.getDepth(root.right, depth+1))
        elif root.left != None and root.right == None: 
            return self.getDepth(root.left, depth+1)
        elif root.left == None and root.right != None: 
            return self.getDepth(root.right, depth+1)