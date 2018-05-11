## [Leetcode#380] Insert Delete GetRandom O(1)
##
## Google, Uber, Amazon, Facebook, Twitter, Yelp
##
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import random
        self.items = set({})
        self.random = random

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.items:
            self.items.add(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.items:
            return False
        else:
            self.items.remove(val)
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = self.random.randint(0, len(self.items)-1)
        
        return list(self.items)[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        