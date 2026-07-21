#
# 666. Path Sum IV
# 
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        full binary tree = {layer: {pos: val}}
        e.g. [113, 215, 221, 319, 324, 343]
              3
            /   \
           5     1
          / \     \
         9   4     3
        {1: {1: 3}, 2: {1: 5, 2: 1}, 3: {1: 9, 2: 4, 4: 3}}

        e.g. [111,217,221,315,415]
                  1
                /   \
               7     1
              /
             5
            /
           5 
         {1: {1: 1}, 2: {1: 7, 2: 1}, 3: {1: 5}, 4: {1: 5}}
        """
        tree = {}
        for num in nums:
            s = str(num)
            layer, pos, val = int(s[0]), int(s[1]), int(s[2])
            if layer not in tree:
                tree[layer] = {pos: val}
            else:
                tree[layer][pos] = val

        self.ans = 0
        def dfs(layer, pos, path_sum):

            path_sum += tree[layer][pos]

            is_leaf = True
            for i in range(2):
                next_pos = 2 * pos - i
                if layer + 1 in tree and next_pos in tree[layer+1]:
                    is_leaf = False
                    dfs(layer+1, next_pos, path_sum)
            
            if is_leaf:
                # if the node is leaf, mean no correspoding childs.
                # return
                self.ans += path_sum

        dfs(1, 1, 0)
        return self.ans
        