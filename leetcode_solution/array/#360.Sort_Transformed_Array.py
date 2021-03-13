#  360. Sort Transformed Array (medium)
#  https://leetcode.com/problems/sort-transformed-array/
#
class Solution:
    '''
    f(x) = ax^2 + bx + c = a(x+b/2a)^2 + C, split point = -b/2a
    
    we split fi(x) = f(x < -b/2a), fj(x) = f(x >= -b/2a)by the split point    
    depends on a > 0 or a < 0: fi/fj will be descending/ascending for a > 0, vice versa
    
    needs to considers a = 0, then b > 0 or b < 0 for f(x)
    '''
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        if a == 0: 
            return [b*x + c for x in nums] if b > 0 else [b*nums[i] + c for i in range(len(nums)-1, -1, -1)]
        
        split, split_idx = -0.5*b/a, None
        transf = []
        for i in range(len(nums)):
            if split_idx is None and nums[i] >= split:
                split_idx = i
            transf.append(self.func(nums[i], a, b, c))
        
        if a < 0:
            fi, fj = transf[:split_idx], transf[split_idx:][::-1]
        else:
            fi, fj = transf[:split_idx][::-1], transf[split_idx:]
        
        i, j = 0, 0
        ans = []
        while i <= len(fi)-1 and j <= len(fj)-1:
            if fi[i] <= fj[j]:
                ans.append(fi[i])
                i += 1
            else:
                ans.append(fj[j])
                j += 1
                
        if i <= len(fi)-1:
            return ans + fi[i:]
        elif j <= len(fj)-1:
            return ans + fj[j:]
        
        return ans
    
    def func(self, x, a, b, c):
        return a*(x**2)+b*x+c
            
                
        
        
        