#
#  238. Product of Array Except Self
#  
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def get_product(start, end):
            prod = 1
            for i in range(start, end):
                prod *= nums[i]
            return prod

        prod = get_product(1, len(nums))
        res = [prod]
        i = 1
        while i < len(nums):
            if nums[i] != 0:
                prod = int(prod / nums[i]) * nums[i-1]
            else: # e.g. [-1,1,0,-3,3] and i = 2
                prod = get_product(0, i) * get_product(i+1, len(nums))

            res.append(prod)
            i += 1

        return res