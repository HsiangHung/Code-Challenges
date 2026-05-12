#  740. Delete and Earn (medium)
#  https://leetcode.com/problems/delete-and-earn/
#
class Solution:
    '''
    e.g. nums = [2,2,3,3,3,4]
    we can take 4 first but need to delete 3 => remaining [2,2] => earn 4+2*2 = 8
    instead take 3 first, delete 2 and 4 => remaining [3,3] => earn 3 + 3 + 3 = 9

    sol: prepare dict {2: 2, 3: 3, 4: 1}, and sorted the key [4,3,2]

    dp[0] = 4
    dp[1] = max(dp[0], 3*3), since 3 = 4-1
    dp[2] = max(dp[1], 2*2+dp[0]), since 2 = 3-1

    if keys = [7,4,2], we can directly earn all points.
    '''
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        nums_dict = {}
        for x in nums:
            nums_dict[x] = nums_dict.get(x, 0) + 1
            
        nums = sorted(nums_dict.keys(), reverse=True) # sort the key
        
        dp = {-1:0, 0: nums_dict[nums[0]]*nums[0]}
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1] - 1:
                dp[i] = max(dp[i-1], dp[i-2] + nums_dict[nums[i]]*nums[i])
            else:
                dp[i] = dp[i-1] + nums_dict[nums[i]]*nums[i]            
            i += 1
            
        return dp[len(nums)-1]
            