#  501. Find Mode in Binary Search Tree (easy)
#  https://leetcode.com/problems/find-mode-in-binary-search-tree/
#
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        mode = {}
        def helper(root: TreeNode) -> None:
            if not root:
                return
            mode[root.val] = mode.get(root.val, 0) + 1
            helper(root.left)
            helper(root.right)

        helper(root)
        max_freq = max([mode[x] for x in mode])
        return [x for x in mode if mode[x] == max_freq]
