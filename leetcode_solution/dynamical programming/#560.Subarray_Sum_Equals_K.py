#  560. Subarray Sum Equals K (medium)
#  https://leetcode.com/problems/subarray-sum-equals-k/
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        NOTE: the array elements could be negative
        time complexity O(N), space complexity O(N) solution:
        a. https://blog.csdn.net/fuxuemingzhu/article/details/82767119?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase
        b. https://www.youtube.com/watch?v=HbbYPQc-Oo4
        
        index i:    0  1  2  3   4  5  6  7
           array = [3, 4, 7, 2, -3, 1, 4, 2]  k =7
        prefix_sum  3  7 14 16  13 14 18 20
            
        when prefix_sum - k exists in prefix_sum set, there exists a subarray with sum=7
             sum(0, 1); sum(2,2); at i=5, prefix_sum-7 = 7 and 7 exists in set;
             at i=7, prefix_sum-7 = 13 and 13 exists in set
        return 4
        
        need to save prefix_sum as dictionary and count.
        e.g. corner case: [0,0,0,0,0,0]
        '''
        num_subarray=0
        
        subsum_dict = {0: 1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in subsum_dict:
                num_subarray += subsum_dict[prefix_sum-k]
            subsum_dict[prefix_sum] = subsum_dict.get(prefix_sum, 0) + 1
            
        return num_subarray