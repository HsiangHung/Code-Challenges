#
# 605. Can Place Flowers
#
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            # We can only consider planting if the current plot is empty
            if flowerbed[i] == 0:
                
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    # Plant a flower here to prevent future adjacent plantings
                    flowerbed[i] = 1
                    n -= 1
                    # Early exit: if we've planted enough flowers, stop searching
                    if n == 0:
                        return True
                        
        return n <= 0 # If we finished the loop and n is still > 0, we failed
