#  95. Unique Binary Search Trees II (medium)
#  https://leetcode.com/problems/unique-binary-search-trees-ii/
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        inspired by 96. Unique Binary Search Trees and the explanation:
        https://www.youtube.com/watch?v=OIc0mHgHUww
        
        Need to do recursion unitl child nodes is None or single list
        
        e.g. [1,2,3,4]
        
             1             2            3            4
            / \           / \          / \          / \
          []  [2,3,4]   [1] [3,4]  [1,2] [4]  [1,2,3]  []

        NOTE: return a list of nodes, and when build a new tree, loop through 
              node for left list and node right list, where each node is a BST
        '''
        if n == 0: return []
        
        nodes = [i+1 for i in range(n)]
        return self.DFS(nodes)
    
    def DFS(self, nodes):
        if len(nodes) == 0: return [None]
        if len(nodes) == 1: return [TreeNode(val=nodes[0])]
        
        ans = []
        for i in range(len(nodes)):
            
            left_BST, right_BST = self.DFS(nodes[:i]), self.DFS(nodes[i+1:])
            
            for left in left_BST:
                for right in right_BST:
                    root = TreeNode(val=nodes[i])
                    root.left, root.right = left, right
                    ans.append(root)        
        return ans