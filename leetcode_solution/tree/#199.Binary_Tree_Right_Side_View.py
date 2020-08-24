## [Leetcode#199] Binary Tree Right Side View
##
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.view = []
        self.DFS(root, 0)
        return self.view
        
    def DFS(self, root, depth):
        if not root: return 
        depth += 1
        
        if len(self.view) < depth:
            self.view.append(root.val)
        else:
            self.view[depth-1] = root.val
        
        self.DFS(root.left, depth)
        self.DFS(root.right, depth)