#  565. Array Nesting (medium)
#  https://leetcode.com/problems/array-nesting/
#
class Solution:
    '''
    when index is visited, removing from index_dict, which saves time by avoid vitisted sites 
    '''
    def arrayNesting(self, nums: List[int]) -> int:
        
        idx_dict = {}
        for i, num in enumerate(nums):
            idx_dict[num] = i
      
        max_seq= 0
        for i in range(len(nums)):
            
            seq = 0
            while i in idx_dict:
                seq += 1
                idx = idx_dict[i]
                del idx_dict[i]
                i = idx

            max_seq = max(max_seq, seq)
            
        return max_seq
            
            
    