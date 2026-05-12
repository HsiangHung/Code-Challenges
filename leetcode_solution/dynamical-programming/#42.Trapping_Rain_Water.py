# 42. Trapping Rain Water (hard)
# https://leetcode.com/problems/trapping-rain-water/
#
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        good explanation: https://www.youtube.com/watch?v=KV-Eq3wYjxI
        
        e.g. height = [0,1,0,2,1,0,1,3,2,1,2,1]
        
        L = MaxHeightofLeftSide  = [0,0,1,1,2,2,2,2,3,3,3,3] 
        R = MaxHeightofRightSide = [3,3,3,3,3,3,3,2,2,2,1,0] 
        
        L[i] stores the max height of left side of the i-th bar 
        R[i] stores the max height of right side of the i-th bar
        
        water traped at i = Min(L[i], R[i]) - height[i] if trap > 0
        '''
        
        left = [0]
        right = [0]
        
        max_height = 0  # left side
        for i in range(1, len(height)):
            max_height = max(max_height, height[i-1])
            left.append(max_height)
            
        max_height = 0  # right side
        for i in range(len(height)-2, -1, -1):
            max_height = max(max_height, height[i+1])
            right.insert(0, max_height)
     
        water = []
        for i in range(len(height)):
            trap = min(left[i], right[i]) - height[i]
            if trap < 0:
                water.append(0)
            else:
                water.append(trap)
                
        return sum(water)