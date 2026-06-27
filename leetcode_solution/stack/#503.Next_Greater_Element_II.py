#
# 503. Next Greater Element II
#
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        stack inspired by https://www.youtube.com/watch?v=sDKpIO2HGq0

        nums = [1,2,5,3,2,6,2], ans = [2,5,6,6,6,-1,5]
          index 0 1 2 3 4 5 6

        ans is initiallized as [-1,-1,-1,-1,-1,-1]

        Using steack, which only inserts index smaller than prev:
        i   prev  nums[i]   stack                         ans
        0           1       []  + [0]     ->  [0]         [-1,-1,-1,-1,...]
        1    1  <   2       [0] + [1]     ->  [1]  pop 0  [2,-1,-1,-1,...]
        2    3  <   5       [1] + [2]     ->  [2]  pop 1  [2,5,-1,-1,...]
        3    5  >   3       [2] + [3]     ->  [2,3]       [2,5,-1,-1,..]
        4    3  >   2       [2,3] + [4]   ->  [2,3,4]     [2,5,-1,-1,..]
        5    2  <   6       [2,3,4] + [5] ->  [2,3] pop 4  [2,5,-1,-1,6,-1,-1]
                            [2,3] + [5]  ->   [2]   pop 3  [2,5,-1,6,6,6,-1,-1]
                            [2] + [5]    ->   [5]   pop 2  [2,5,6,6,6,-1,-1]
        6    6  >   2       [5] + [6]    ->   [5,6]     

        by circular array, i=6 willl meet 5, [2,5,6,6,6,-1,5]
        """

        n = len(nums)
        ans = [-1] * n

        stack = [0]
        i = 1
        for i in range(2 * n):
            # need to run 2*n instead n, due to circular array
            idx = i % n
            while len(stack) > 0 and nums[idx] > nums[stack[-1]]:
                larger_idx = stack.pop()
                ans[larger_idx] = nums[idx]
            stack.append(idx)

        return ans
