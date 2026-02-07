## [Leetcode#102] Binary Tree Level Order Traversal
##
## Facebook, Amazon, Microsoft, Bloomberg, Apple, LinkedIn
##
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        traversal = []
        bfs = [(root, 0)]
        while len(bfs) > 0:
            node, layer = bfs.pop(0)
            
            if layer > len(traversal) - 1:
                traversal.append([])
            traversal[layer].append(node.val)

            if node.left:
                bfs.append((node.left, layer + 1))
            if node.right:
                bfs.append((node.right, layer + 1))
        
        return traversal
