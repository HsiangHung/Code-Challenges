#  1352. Product of the Last K Numbers (medium)
#  https://leetcode.com/problems/product-of-the-last-k-numbers/
#
class ProductOfNumbers:
    '''
    need to worry about in add method, new-incoming element "num" = 0 or 1 or others
    
    1. if "num" = 0, need to set to zero in all prefix products
    2. if "num" = 1, do nothing
    3. if "num" != 0 and "num" != 1, multiply all prefixs with "num", and append to self.product
    
    Note to save more time, we need to keep "zero_offset" where zero prefix starts, and only update i > "zero_offset".
    
    e.g. initially self.zero_offset = 0
    
                  self.product
    [2]           [2]
    [2,3]         [6,3]
    [2,3,4]       [24,12,4]
    [2,3,4,0]     [0,0,0,0]       now we assign "zero_offset" = 4
    [2,3,4,0,5]   [0,0,0,0,5]
    [2,3,4,0,5,2] [0,0,0,0,10,2]
    
    '''
    def __init__(self):
        self.product = []
        self.zero_offset = 0

    def add(self, num: int) -> None:
        
        if len(self.product) > 0:
            if num != 0 and num != 1:
                for i in range(self.zero_offset, len(self.product)):
                    self.product[i] = self.product[i]*num
            elif num == 0:
                for i in range(self.zero_offset, len(self.product)):
                    self.product[i] = 0
                self.zero_offset = len(self.product)
        
        self.product.append(num)
        
        
    def getProduct(self, k: int) -> int:        
        return self.product[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)