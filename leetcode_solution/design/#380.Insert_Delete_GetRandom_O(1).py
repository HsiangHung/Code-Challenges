# #380. Insert Delete GetRandom O(1)
#
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set({})

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums:
            return False
        else:
            self.nums.add(val)
            return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        if len(self.nums) >= 1:
            return random.sample(self.nums, 1)[0]
        else:
            return False

    def getRandom2(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        if len(self.set) >= 1:
            return list(self.set)[random.randint(0, len(self.set)-1)]
        else:
            return False


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()