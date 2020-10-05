# # 173. Binary Search Tree Iterator
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
        self.push_left(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        print ([x.val for x in self.nodes])
        
        root = self.nodes.pop()
        self.push_left(root.right)
            
        return root.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.nodes) == 0: return False
        
        return True

    def push_left(self, node):
        
        while node:
            self.nodes.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()