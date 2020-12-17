#  958. Check Completeness of a Binary Tree
#  https://leetcode.com/problems/check-completeness-of-a-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    In the same layer, there should no nodes exist before the last nodes.
    e.g.    
             1                      1
            / \        or          / 
           2   5                  2   
          /   / \                /
         3   7   8              3

    are not complete trees.
    '''
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return root
        
        queue = [(root, 0)]
        
        while queue:
                  
            if queue[0] is not None:
                node, depth = queue.pop(0)
                
                if node.left: 
                    queue.append((node.left, depth+1))
                else:
                    queue.append(None)
                
                if node.right: 
                    queue.append((node.right, depth+1))
                else:
                    queue.append(None)
            else:
                
                i = 0
                while i <= len(queue)-1 and queue[i] == None:
                    i += 1
                
                if i <= len(queue)-1: 
                    return False
                else:
                    return True
                
        return True
