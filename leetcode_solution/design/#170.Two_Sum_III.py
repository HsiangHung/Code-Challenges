# #170. Two Sum III - Data structure design
#
class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] = self.nums.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value % 2 == 1:
            for num in self.nums:
                if value - num in self.nums: return True
        else:
            for num in self.nums:
                if num != value // 2:
                    if value - num in self.nums: return True
                else:
                    if self.nums[num] > 1: return True
        return False
    


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)