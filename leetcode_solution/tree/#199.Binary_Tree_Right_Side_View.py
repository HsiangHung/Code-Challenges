#  199. Binary Tree Right Side View (medium)
#  https://leetcode.com/problems/binary-tree-right-side-view/
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class BFSSolution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        views = []
        queue = [(root, 1)]
        while queue:            
            node, depth = queue.pop(0)
            
            if len(views) < depth:
                views.append(node.val)
            else:
                views[depth-1] = node.val
                
            if node.left: queue.append((node.left, depth+1))
            if node.right: queue.append((node.right, depth+1))
                
        return views
            
#
class DFSSolution(object):
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