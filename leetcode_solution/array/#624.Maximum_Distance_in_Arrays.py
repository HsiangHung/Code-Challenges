## [Leetcode#624] Maximum Distance in Arrays
##
#
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        ## all subarray are sorted, so take the first and last element and put them in hashtable
        
        num_dict = {}
        for i in range(len(arrays)):
            for j in [0, -1]:
                if arrays[i][j] not in num_dict:
                    num_dict[arrays[i][j]] = set({i})
                else:
                    num_dict[arrays[i][j]].add(i)
                
        nums = sorted(num_dict.keys())
        
        ## all numbers are in sorted and the maximum distance comes from largest and smallest,
        ## but needs both of them came from different subarray so need num_dict[val] be different
        max_val, min_val = nums[-1], nums[0]
        max_dist = None
        i = 0
        while max_dist == None and i <= len(nums)-1:
            max_val, min_val = nums[-1-i], nums[0]
            if num_dict[max_val] != num_dict[min_val] or len(num_dict[max_val]) > 1:
                max_dist = abs(nums[-1-i]-nums[0])

            max_val, min_val = nums[-1], nums[i]
            if num_dict[max_val] != num_dict[min_val]:
                max_dist = max(max_dist, abs(nums[-1]-nums[i]))

            i += 1
                 
        return max_dist      