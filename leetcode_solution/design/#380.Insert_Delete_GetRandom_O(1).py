# #380. Insert Delete GetRandom O(1)
#
class RandomizedSet:
    '''
    https://blog.csdn.net/mebiuw/article/details/52563529
    two data structures:
    data = {va1: idx1, va2: idx2,....}, array = [v1, v2, ....]
    
    if remove val == self.array[-1]:
        del data[val] and array.pop()
    else:
        array = [..., val, .....x] => SWAP => array = [..., x,.... val]
        update data[x] index to the val's index, and array[val's index] = x
        then still del data[val] and array.pop() 
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        idx = len(self.array)
        if val in self.data:
            return False
        else:
            self.data[val] = idx
            self.array.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        else:
            if val == self.array[-1]:
                del self.data[val]
            else:
                idx = self.data[val]
                del self.data[val]

                last_val = self.array[-1]
                self.array[idx] = last_val
                self.data[last_val] = idx

            self.array.pop()
                      
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return self.array[random.randint(0, len(self.array)-1)]


class RandomizedSet2:

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