# [#379] Design Phone Directory
#
# google
#
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.items = set({})
        for i in range(maxNumbers-1, -1, -1):
            self.items.add(i)
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.items) == 0: return -1
        
        for num in self.items:
            self.items.remove(num)
            break 
        return num
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.items
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.items.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)