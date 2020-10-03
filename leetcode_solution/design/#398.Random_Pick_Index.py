# #398. Random Pick Index
#
class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            self.dict[nums[i]] = self.dict.get(nums[i], []) + [i]
            
    def pick(self, target: int) -> int:
        import random
        
        random_pick = random.randint(0, len(self.dict[target])-1)
        # NOTE: random.randint(a, b) select a <= x <= b, so need len(..)-1
        return self.dict[target][random_pick]
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)