# #416. Partition Equal Subset Sum
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        time complexity O(n*sum), space O(sum)
        http://bookshadow.com/weblog/2016/10/09/leetcode-partition-equal-subset-sum/

        e.g. nums = [1,5,11,5]
        initialize dp = {0}
        then we have num    dp
                      1     {0, 1}
                      5     {0, 1, 5, 6}
                     11     {0, 1, 5, 6, 11, 12, 16, 17}
                      5     {0, 1, 5, 6, 10, 11, 12, 16, 17, 21, 22}
        '''
        total_sum = sum(nums)
        
        if total_sum % 2 == 1: return False
        
        dp = set({0})
        for num in nums:
            for x in dp.copy():  ## note, set.copy(), otherwise chaing set size.
                dp.add(x+num)
                
        return total_sum/2 in dp
            
        
        