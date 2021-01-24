#  698. Partition to K Equal Sum Subsets (medium)
#  https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
#
class Solution:
    '''
    inspired by the Youtube: https://www.youtube.com/watch?v=O17fztIRR3I
    
    we prepare partitions = [0, 0, 0, 0]
    if nums is sorted in descresing order, [4,3,2,3,5,2,1] -> [5,4,3,3,2,2,1] then we can pass
    since in this case we can fill the larger numbers in partitions first.
    
    If partitions[i] >= target value of subsets, we skip to next
    
    0 0 0 0 [5,4,3,3,2,2,1]
    5 0 0 0   [4,3,3,2,2,1]
    5 4 0 0     [3,3,2,2,1]
    5 4 3 0       [3,2,2,1]
    5 4 3 3         [2,2,1]
    5 4 5 3           [2,1]
    5 4 5 5             [1]
    5 5 5 5              [] return True
    
    '''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False
        
        target = sum(nums) // k
        partitions = [0]*k
        return self.DFS(partitions, sorted(nums, reverse=True), target) # NOTE: sorted reversely is trick
        
    def DFS(self, partitions, nums, target):
        if len(nums) == 0:
            return True if set(partitions) == set([target]) else False
        
        for i in range(len(partitions)):
            if partitions[i] + nums[0] <= target:
                partitions[i] += nums[0]
                if self.DFS(partitions, nums[1:], target):
                    return True
                partitions[i] -= nums[0]

        return False