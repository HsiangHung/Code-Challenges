#  173. Binary Search Tree Iterator (medium)
#  https://leetcode.com/problems/binary-search-tree-iterator/submissions/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
    https://blog.csdn.net/fuxuemingzhu/article/details/79436947
    To satisfy the require memoey usage O(h), we need to do the following:
    '''
    def __init__(self, root: TreeNode):
        
        self.nodes = []
        self.goLeft(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        x = self.nodes.pop(0)
            
        if x.right:
            self.goLeft(x.right)
           
        return x.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.nodes) > 0 

    def push_left(self, node):
        if not root: return
        
        self.nodes.insert(0, root)
        
        while root.left:
            root = root.left
            self.nodes.insert(0, root)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()