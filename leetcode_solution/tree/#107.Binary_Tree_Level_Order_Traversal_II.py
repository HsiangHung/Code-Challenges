## [Leetcode#107] Binary Tree Level Order Traversal II
##
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        return self.traverse([], 1, root)[::-1]
    
    def traverse(self, nodeList, depth, root):
        if not root.left and not root.right:
            return self.storeNode(nodeList, depth, root)
        
        nodeList = self.storeNode(nodeList, depth, root)
        
        if root.left:
            nodeList = self.traverse(nodeList, depth+1, root.left)
            
        if root.right:
            nodeList = self.traverse(nodeList, depth+1, root.right)
            
        return nodeList
            
            
    def storeNode(self, nodeList, depth, root):
        if len(nodeList) < depth:
            nodeList.append([root.val])
        else:
            nodeList[depth-1].append(root.val)
        return nodeList