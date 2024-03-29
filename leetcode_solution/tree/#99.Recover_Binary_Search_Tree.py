#  99. Recover Binary Search Tree (medium)
#  https://leetcode.com/problems/recover-binary-search-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/4298069.html
    
    run through tree using in-order and store to an array O(n) space.
    Then use O(n) time to search wrong order.
    if one pair wrong, (i-1, i), (i-1, i) -> (i, i-1), e.g. [3,1,4,null,null,2]
    if two pairs wrong, (i-1, i), (j-1, j), (i, j) -> (j, i), e.g. [1,3,null,null,2]
    '''
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = {}
        nodes = self.DFS(root)
                
        wrong, i = [], 1
        while i <= len(nodes)-1 and len(wrong) < 2:
            if nodes[i].val < nodes[i-1].val:
                wrong.append((i-1, i))
            i += 1

        if len(wrong) == 1:  # case I: i-1, i switch
            a, b = wrong[0]
        elif len(wrong) == 2: # case II: i, j switch, j >= i+1
            a, b = wrong[0][0], wrong[1][1]
        
        nodes[a].val, nodes[b].val = nodes[b].val, nodes[a].val
        
        return root
        
        
    def DFS(self, root):
        if not root: return []
        node = self.DFS(root.left) + [root] + self.DFS(root.right)
        return node
        
        