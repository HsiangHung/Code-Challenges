# #416. Partition Equal Subset Sum
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        time complexity O(n*sum), space O(sum)
        http://bookshadow.com/weblog/2016/10/09/leetcode-partition-equal-subset-sum/
        '''
        total_sum = sum(nums)
        
        if total_sum % 2 == 1: return False
        
        sum_set = set({0})
        for num in nums:
            for x in sum_set.copy():  ## note, set.copy(), otherwise chaing set size.
                sum_set.add(x+num)
                
        return total_sum/2 in sum_set
            
        
        