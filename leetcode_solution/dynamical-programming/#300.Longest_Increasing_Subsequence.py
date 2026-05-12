# #300. Longest Increasing Subsequence
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Brutal force: 2^n
        DP: time complexity O(n^2), space complexity O(n^2)
        https://www.youtube.com/watch?v=fV-TF4OvZpk
        
        * loop through all n, for each subsarry nums[: n], find optimal solution.
        e.g. nums = [9,2,5,3,7,101,18,20,1,2,30,5]
             dp.  = [1,1,1,1,1,  1, 1, 1,1,1, 1,1]
             start j=1, nums[1]=2: 2 < 9, so doesn't update dp["2"]
                   j=2, nums[2]=5: 5 < 9, but 5 > 2, so update dp["5"] = dp["2"]+1=2
                   j=3, nums[3]=3: 3 < 9, 3 > 2, 3 < 5, dp["3"] = dp["2"]+1 = 2
                   j=4, nums[4]=7: 7 > 3 or 7 > 5, dp["7"]=dp["3"]+1=3 or dp["7"]=d["5"]+1=3
                   j=5, nums[5]=101: 101>7, dp["101"]=dp["7"]+1=4
                   ....
                   j=10, nums[10]=30: 30>20, dp["30"]=dp["20"]+1=6 (dp["20"] has maximum)
                   j=11, nums[11]=5: only 5>2, so dp["5"]=d["2"]+1=2
        '''
        if nums == []: return 0
        
        self.dp = [1]*len(nums)
        
        max_seq_len = 1
        for i in range(1, len(nums)):
            max_seq_len = max(max_seq_len, self.get_max_sequence(nums[: (i+1)]))
           
        return max_seq_len
    
    
    def get_max_sequence(self, nums):
        '''
        look for optimal len of subsequence, by nums[:j]
        '''
        idx = len(nums)-1        
        for j in range(len(nums)-1):
            if nums[-1] > nums[j]:
                self.dp[idx] = max(self.dp[idx], self.dp[j] + 1)
        
        return self.dp[idx]
        
        
        
        
        