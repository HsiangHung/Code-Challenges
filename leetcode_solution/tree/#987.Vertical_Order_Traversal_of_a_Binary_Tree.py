#  987. Vertical Order Traversal of a Binary Tree (medium)
#  https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BFS_Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        queue = [(root, 0, 0)]
        position = {}
        while queue:
            node, x, y = queue.pop(0)
            
            if x not in position:
                position[x] = {y: [node.val]}
            else:
                position[x][y] = position[x].get(y, []) + [node.val]
            
            if node.left: queue.append((node.left, x-1, y+1))
            if node.right: queue.append((node.right, x+1, y+1))
                
        ans = []
        for x in sorted(position.keys()):
            views = []
            for y in sorted(position[x].keys()):
                views += sorted(position[x][y])
            ans.append(views)
        return ans
#
#
class DFS_Solution:
    def __init__(self):
        self.position = {}
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        '''
        save data as dict = {x:{y1:[a, b], y2: [c]}..} 
        '''
        if not root: return []
        
        self.xy = {}
        self.DFS(root, 0, 0)
        
        ans = []
        for x in sorted(self.xy.keys()):
            trav = []
            for y in sorted(self.xy[x].keys()):
                trav += sorted(self.xy[x][y])
            ans.append(trav)
        return ans
        
    def DFS(self, root, x, y):
        if not root: return 
        
        if x not in self.xy:
            self.xy[x] = {}
        
        self.xy[x][y] = self.xy[x].get(y, []) + [root.val]
            
        self.DFS(root.left,  x-1, y+1)
        self.DFS(root.right, x+1, y+1)
         
        