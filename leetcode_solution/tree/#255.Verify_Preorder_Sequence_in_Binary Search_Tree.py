## [Leetcode#255] Verify Preorder Sequence in Binary Search Tree
#
# zenefit
#
#
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        #
        # https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
        # note [10,5,2,4,12] still true since the tree could be [10,5,12,2,null,null,null,null,4] (BFS)
        # not [10,5,12,2,4] (BFS)
        #
        stack = []
 
        # Initialize current root as minimum possible value
        min_val = -float('inf')
 
        # Traverse given array
        for x in preorder: 
        
            if x < min_val:
                return False

            while(len(stack) > 0 and stack[-1] < x) :
                min_val = stack.pop()

            stack.append(x)
            
        return True
 