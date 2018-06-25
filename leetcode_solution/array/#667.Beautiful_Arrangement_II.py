## [#667] Beautiful Arrangement II
#
#
#
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        #
        # idea: this is pretty simple. 
        # e.g. n =7 so we have nums [1,2,3,4,5,6,7] and k =5
        # always start from 1, and 1+5 = 6, and 6-4 =2, and 2+3=5, and..
        # such that [1,6,2,5,3,4]; the difference is [5,-4,3,-2,1] and remaining [7] 
        # so return [1,6,2,5,3,4] + [7]
        #
        if k == 1:
            return range(1, n+1)
        
        nums = set(range(1, n+1))
        arr = [1]
        nums.remove(1)
        sgn = 1
        for k in range(k, 0, -1):
            num = arr[-1]+ sgn *k
            arr.append(num)
            nums.remove(num)
            sgn *= -1
            
        if (nums) > 0:
            arr += list(nums)
            
        return arr