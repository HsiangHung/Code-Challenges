#  713. Subarray Product Less Than K (medium)
#  https://leetcode.com/problems/subarray-product-less-than-k/
#
class Solution:
    '''
    http://bookshadow.com/weblog/2017/10/22/leetcode-subarray-product-less-than-k/
    
    e.g. nums = [10, 5, 2, 6, 1, 8, 2]
    
    R moving forward if product < k still, otherwise L moving forward
    
                             L  R     count    subarray
    [10]                    -1  0      +1      [10]
    [10, 5]                 -1  1      +2      [10,5], [5]
    [10, 5, 2]               > k
        [5, 2]               1  2      +2      [5,2], [2]
        [5, 2, 6]            1  3      +3      [5,2,6], [2,6], [6]
        [5, 2, 6, 1]         1  4      +4      [5,2,6,1], [2,6,1], [6,1], [1]
        [5, 2, 6, 1, 8]      > k
           [2, 6, 1, 8]      2  5      +4      [2,6,1,8], [6,1,8], [1,8], [8]
           [2, 6, 1, 8, 2]   > k      
              [6, 1, 8, 2]   3  6      +4      [6,1,8,2], [1,8,2], [8,2], [2]
        
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        prod = 1
        L = R = -1
        
        count = 0
        for num in nums:
            R += 1
            prod *= num
            while L + 1 <= R and prod >= k:
                prod /= nums[L+1]
                L += 1
                
            count += R - L
            
        return count