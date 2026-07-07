#  560. Subarray Sum Equals K (medium)
#  https://leetcode.com/problems/subarray-sum-equals-k/
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        build a dict to collect prefix_sum with key of prefix_sum - k
        if the key exist, meaning during process, there exist subarray sum = k
        ref: https://www.youtube.com/watch?v=HbbYPQc-Oo4

        e.g. nums = [3,4,7,2,-3,1,4,2], k=7, ans = 4 ([3,4],[7],[7,2,-3,1],[1,4,2])

         x  sum  ans  sum-k  prefix_sum_dict
              0    0         {0: 1}
         3    3    0     -4  {0: 1, 3: 1}
         4    7    1      0  {0: 1, 3: 1, 7: 1}   we have [3,4] and sum-k=0. so ans=1
         7   14    2      7  {0: 1, 3: 1, 7: 1, 14: 1}  we have [7], for sum-k=7, so ans=2
         2   16    2      9  {0: 1, 3: 1, 7: 1, 14: 1, 16: 1}
        -3   13    2      6  {0: 1, 3: 1, 7: 1, 14: 1, 16: 1, 13: 1}
         1   14    3      7  {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1}, sum=14 & sum-k exist, from [3,4,7] -> [3,4,7,2,-3,1], difference [2,-3,1]
         4   18    3     11  {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1}, 
         2   20    4     13   sum=20 & sum-k=13 exist, from [3,4,7,2,-3,1] -> [3,4,7,2,-3,1,4,2], difference is [1,4,2]
        """

        ans = 0
        prefix_sum = 0
        presum_dict = {0: 1}
        for x in nums:
            prefix_sum += x

            if prefix_sum - k in presum_dict:
                ans += presum_dict[prefix_sum - k]
            
            presum_dict[prefix_sum] = presum_dict.get(prefix_sum, 0) + 1

        return ans