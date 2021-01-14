#  486. Predict the Winner (medium)
#  https://leetcode.com/problems/predict-the-winner/
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/6369688.html (use recursion approach)
    
    MIniMax: https://brilliant.org/wiki/minimax/
    '''
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def DFS(player, nums, sum1, sum2):
            if len(nums) == 1:               
                return sum1 + nums[0] >= sum2 if player == 1 else sum2 + nums[0] > sum1
            
            if player == 1:
                return not DFS(2, nums[1:], sum1+nums[0], sum2) or not DFS(2, nums[:-1], sum1+nums[-1], sum2)
            else:
                return not DFS(1, nums[1:], sum1, sum2+nums[0]) or not DFS(1, nums[:-1], sum1, sum2+nums[-1])
            
        if len(nums) == 1: return True
        
        return DFS(1, nums, 0, 0)
        
            
