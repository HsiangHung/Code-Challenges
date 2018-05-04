## [Leetcode#605] Can Place Flowers
##
##
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: return True
        
        ## the idea: if there are neigbors of an empty spot == 1
        ##           change to 2. e.g. [0,1,0,0,0,1,0] => [2,1,2,0,2,1,2]
        ##           then we can easily see the only available spot is only one.
        

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i-1] == 1:
                    flowerbed[i] = 2
                
                if i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                    flowerbed[i] = 2
            
                if flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1        
                
                if n == 0: return True
            
        return False
                