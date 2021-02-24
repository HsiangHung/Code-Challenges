#  863. All Nodes Distance K in Binary Tree (medium)
#  https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:      
    '''
    I don't know why this problem is evaluated as medium. Should be hard.
    Three parts:
     * 1. "tree_traverse", if hit the target, "get_child" continues search childs distance = K for root.
     * 2. during tree traverse, store graph connection, including root -> child, and root -> parent
          (bidirectional graph) in self.graph 
     * 3. "graph_traverse" by K -= 1 until K = 0
     
    e.g. root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    
    after *1, we will have self.candidates = {4, 7} 
                           self.graph = {3:[5,1], 5:[3], 1:[3,0,8], 0:[1], 8:[1]}
          then use graph_traverse and self.graph to find nodes which are in other branches.
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:    
        if not root: return 0
        
        if K == 0: return [target.val]
        
        self.candidates = set({})
        self.graph = {}
        self.target_path = None
        
        self.tree_traverse(root, target, K)        
        self.graph_traverse(target.val, target.val, K, set({}))
        
        return list(self.candidates)

    def graph_traverse(self, target, i, K, visited): 
        if i in visited: return
    
        if K == 0:
            if i != target: self.candidates.add(i)
            return

        visited.add(i)
        if i in self.graph:
            for x in self.graph[i]:
                self.graph_traverse(target, x, K - 1, visited.copy())
        
        
    def tree_traverse(self, root, target, K):
        if not root.left and not root.right: return
           
        if root.val == target.val:
            self.get_child(root, K)
            return
        
        if root.left:
            self.graph[root.val] = self.graph.get(root.val, []) + [root.left.val]
            self.graph[root.left.val] = self.graph.get(root.left.val, []) + [root.val]
            self.tree_traverse(root.left, target, K)
            
        if root.right:
            self.graph[root.val] = self.graph.get(root.val, []) + [root.right.val]
            self.graph[root.right.val] = self.graph.get(root.right.val, []) + [root.val]
            self.tree_traverse(root.right, target, K)
      

    def get_child(self, root, K):
        if K == 0: 
            self.candidates.add(root.val)
            return 
            
        if not root.left and not root.right: return
        
        if root.left:
            self.get_child(root.left, K-1)
        
        if root.right:
            self.get_child(root.right, K-1)
            
            