#  114. Flatten Binary Tree to Linked List (medium)
#  https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
#  Microsoft
#
class Solution(object):
    '''
    I found using BFS and instead append, insert to index = 0 is a much easier way.
    e.g. tree = [1,2,5,3,4,null,6], initial queue = [1]
               1
              / \
             2   5   
            / \   \
           3   4   6

         queue   node pop  after pop    queue'
         [1]      1          []      -> [2,5]
         [2,5]    2          [5]     -> [3,4,5]
         [3,4,5]  3          [4,5]   -> [4,5]
         [4,5]    4          [5]     -> [5]
         [5]      5          []      -> [6]
         [6]      6          done

         We can see the popped node.right = queue[0] to flaten
    '''
     def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            if node.right: queue.insert(0, node.right)
            if node.left:  queue.insert(0, node.left)
            
            node.right = queue[0] if len(queue) > 0 else None
            node.left = None


#
# DFS solution: return last node of each branch (left_last, right_last)
#
class DFSSolution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right): return root
        
        left, right = root.left, root.right
        root.left = None
        
        if left and right:
            left_last, right_last = self.flatten(left),  self.flatten(right)
            root.right = left
            left_last.right = right
            return right_last
        elif left:
            left_last = self.flatten(left)
            root.right = left
            return left_last
        else:
            right_last = self.flatten(right)
            return right_last
