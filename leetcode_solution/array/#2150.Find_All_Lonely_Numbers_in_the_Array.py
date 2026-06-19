#
# 2150. Find All Lonely Numbers in the Array
#
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        num_dict = {}
        for x in nums:
            num_dict[x] = num_dict.get(x, 0) + 1

        res = []
        for x in num_dict:
            if num_dict[x] == 1 and (x - 1 not in num_dict) and (x + 1 not in num_dict):
                res.append(x)
    
        return res