# #987. Vertical Order Traversal of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.position = {}
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        '''
        save data as dict = {x:{y1:[a, b], y2: [c]}..} 
        '''
        if not root: return []
     
        self.DFS(0, 0, root)
    
        output = []
        for x in sorted(self.position.keys()):
            same_x = []
            for y in sorted(self.position[x]):
                if len(self.position[x][y]) > 1:
                    same_x += sorted(self.position[x][y]) 
                else:
                    same_x += self.position[x][y]
            output.append(same_x)
                
        return output
        
        
    def DFS(self, x, y, root):
        
        if not root: return 
        
        if x in self.position: 
            if y in self.position[x]:
                self.position[x][y].append(root.val)
            else:
                self.position[x][y] = [root.val]
        else:
            self.position[x] = {y: [root.val]}
        
        self.DFS(x-1, y+1, root.left)
        self.DFS(x+1, y+1, root.right)
        
        