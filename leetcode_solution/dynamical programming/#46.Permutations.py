## [#46] Permutations
#   
#  Microsoft, LinkedIn
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return [nums]

        dp = [[nums[0]]]
        nums_len = 2
        while nums_len <= len(nums):
            insert_elm = nums[nums_len-1]
            
            pertmut = []
            for sublist in dp:
                for i in range(len(sublist)+1):
                    new_sublist = sublist[:]
                    new_sublist.insert(i, insert_elm)
                    pertmut.append(new_sublist)
                    
            dp = pertmut
            nums_len += 1
            
        return dp