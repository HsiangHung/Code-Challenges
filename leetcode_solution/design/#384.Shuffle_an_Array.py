#  384. Shuffle an Array (medium)
#  https://leetcode.com/problems/shuffle-an-array/
#
class Solution:

    def __init__(self, nums: List[int]):       
        self.default = nums[:]
        self.data = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """        
        return self.default

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        
        ans = []
        while self.data:
            ans.append(self.data.pop(random.randint(0, len(self.data)-1)))
            
        self.data = ans[:]
            
        return ans
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()