# [#515] Find Largest Value in Each Tree Row
#
# 
#
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        NOTE BFS is easier for such problem
        """
        if not root:
            return []

        ans = []
        bfs = [(root, 0)]
        while bfs:
            node, layer = bfs.pop(0)

            if len(ans) == layer:
                ans.append(node.val)
            else:
                ans[layer] = max(ans[layer], node.val)

            if node.left:
                bfs.append((node.left, layer + 1))
            if node.right:
                bfs.append((node.right, layer + 1))

        return ans