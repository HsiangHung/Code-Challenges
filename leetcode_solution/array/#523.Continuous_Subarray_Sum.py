# # 523. Continuous Subarray Sum
#
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        http://bookshadow.com/weblog/2017/02/26/leetcode-continuous-subarray-sum/
        '''
        dmap = {0 : -1}
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if k != 0:
                m = Sum % k
            else: 
                m = Sum
            if m not in dmap: 
                dmap[m] = i
            elif i > dmap[m] + 1: 
                return True
        return False