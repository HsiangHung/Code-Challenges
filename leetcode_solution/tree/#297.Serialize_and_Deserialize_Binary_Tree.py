## [Leetcode#297] Serialize and Deserialize Binary Tree
#
# Google, MS, FB, Amazon, Bloomberg, LinkedIn, Uber, Yahoo
#
#
# using BFS to traversal the tree
#
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return str([])
        
        outcome = [root.val]
        
        stack = [root]
        while len(stack) != 0:
            
            node = stack.pop()
            
            if node.left and node.right:
                left, right = node.left, node.right
                stack.insert(0, left)
                stack.insert(0, right)
                outcome += [left.val, right.val]
            elif node.left and not node.right:
                stack.insert(0, node.left)
                outcome += [node.left.val, None]
            elif not node.left and node.right:
                stack.insert(0, node.right)
                outcome += [None, node.right.val]
            else:
                outcome += [None, None]

        return str(outcome)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(",")
        
        if data[0] == "": return None
        
        root = TreeNode(int(data[0]))
        stack = [root]
        for i in range(1, len(data), 2):
            
            if len(stack) > 0:
                node = stack.pop(0)
                left, right = data[i], data[i+1]
                if left != " None": 
                    node.left = TreeNode(int(left[1:]))
                    stack.append(node.left)

                if right != " None": 
                    node.right = TreeNode(int(right[1:]))
                    stack.append(node.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))