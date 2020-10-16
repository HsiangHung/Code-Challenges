# # 314. Binary Tree Vertical Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        This problem is unable to solve using DFS.
        e.g. example 3: [3,9,8,4,0,1,7,null,null,null,2,5]
             using DFS we will obtain [[4],[9,5],[3,0,1],[2,8],[7]], 
             not [[4],[9,5],[3,0,1],[8,2],[7]] since from left, we will
             hit 2 first, not 8
        
        only using BFS we can limit from left to right, from top to bottom
        '''
        if not root: return []
        
        self.col = {}
        
        self.BFS([(root, 0)])
        
        return [self.col[r] for r in sorted(self.col)]
    
    
    def BFS(self, stack):
            
        next_stack = []
    
        while len(stack) > 0:
            node, x = stack.pop(0)
                        
            self.col[x] = self.col.get(x, []) + [node.val]
            
            if node.left:
                next_stack.append((node.left, x-1))
                
            if node.right:
                next_stack.append((node.right, x+1))
        
        if len(next_stack) > 0:       
            self.BFS(next_stack)