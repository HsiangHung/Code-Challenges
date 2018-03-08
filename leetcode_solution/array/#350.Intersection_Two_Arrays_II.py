# [#350] Intersection of Two Arrays II
#
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        space complexity O(n), time O(m)+O(n)
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1
            
        #print nums1_dict
        
        intersect = []
        for num in nums2:
            if num in nums1_dict:
                intersect.append(num)
                if nums1_dict[num] > 1:
                    nums1_dict[num] -= 1
                elif nums1_dict[num] == 1:
                    del nums1_dict[num]
                    
        return intersect
        
        
    