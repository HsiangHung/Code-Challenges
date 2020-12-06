#  1123. Lowest Common Ancestor of Deepest Leaves (medium)
#  https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        '''
        NOTE: could be more than two deepest leaves, like 4 in the testing case.
        [1,3,2,14,10,4,6,null,null,null,11,8,5,9,7,null,null,15,null,16,13,null,null,12]        
        '''
        if not root: return root
        
        self.paths = None
        self.max_depth = -1
        self.DFS(root, [root], 0)
                
        if len(self.paths) == 1:
            return self.paths[0][-1]
        else:
            for i in range(len(self.paths[0])-1, -1, -1):
                ancestors = set([self.paths[j][i] for j in range(len(self.paths))])
                if len(ancestors) == 1: return self.paths[0][i]
        
    def DFS(self, root, path, depth):
        if not root.left and not root.right:
            if depth > self.max_depth:
                self.paths = [path]
                self.max_depth = depth
            elif depth == self.max_depth:
                self.paths.append(path)
            return
        
        if root.left:
            self.DFS(root.left, path + [root.left], depth +1)
            
        if root.right:
            self.DFS(root.right, path + [root.right], depth +1)
