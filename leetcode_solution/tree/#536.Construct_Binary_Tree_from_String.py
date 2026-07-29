#
#  536. Construct Binary Tree from String
#  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """
        node stack. e.g. 4(2(3)(1))(6(5))
        1. [4]
        2. [4, 2] 4.left = 2
        3. [4, 2, 3], 2.left = 3
        4. ")", so pop a node: [4, 2, 3] -> [4, 2]
        5. [4, 2, 1], 2.right = 1
        6. ")", so pop a node: [4, 2, 1] -> [4, 2]
        7. ")" again, so pop a node: [4, 2] -> [4]

        8. [4, 6], 2.right = 6
        9. [4, 6, 5], 6.left = 5
        10. ")", so pop a node: [4, 6, 5] -> [4, 6]
        11. ")" again, so pop a node: [4, 6] -> [4]

        now stack = [4] is root
        """
        if s == "":
            return None

        stack = []
        last_num = ""
        for i in range(len(s)):
            if s[i] == "-" or s[i].isdigit():
                last_num += s[i] # concat "123" = "12"+"3", or "-2" = "-" + "2"
            else:
                if last_num != "":
                    node = TreeNode(val=int(last_num))
                    if len(stack) > 0:
                        parent = stack[-1]
                        if parent.left is None:
                            parent.left = node
                        else:
                            parent.right = node
                    stack.append(node)
                    last_num = ""

            if s[i] == ")":
                stack.pop()
        
        return stack[0] if len(stack) > 0 else TreeNode(val=int(s))