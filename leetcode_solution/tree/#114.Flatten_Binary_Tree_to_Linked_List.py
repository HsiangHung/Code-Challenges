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
        if not root:
            return

        if root.left and root.right:
            l1, l2 = self.flatten(root.left)
            r1, r2 = self.flatten(root.right)
            root.left = None
            root.right = l1
            l2.right = r1
            return root, r2
        elif root.left and not root.right:
            l1, l2 = self.flatten(root.left)
            root.left = None
            root.right = l1
            return root, l2
        elif not root.left and root.right:
            r1, r2 = self.flatten(root.right)
            return root, r2
        else:
            return root, root