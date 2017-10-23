## [Leetcode#661] Image Smoother
##
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        smoothed_M = []
        for y in range(len(M)):
            smoothed_array = []
            for x in range(len(M[0])):
                smoothed_array.append(self.smoothing(M, x, y))
                
            print smoothed_array
            
            smoothed_M.append(smoothed_array)
            
        return smoothed_M
    
    
    def smoothing(self, M, x, y):
        count_sum = M[y][x]
        count = 1
        if x-1 >= 0:
            count_sum += M[y][x-1]
            count += 1
            if y-1 >= 0:
                count_sum += M[y-1][x-1]
                count += 1
            
            if y+1 <= len(M)-1:
                count_sum += M[y+1][x-1]
                count += 1
        
        if x+1 <= len(M[0])-1:
            count_sum += M[y][x+1]
            count += 1
            if y-1 >= 0:
                count_sum += M[y-1][x+1]
                count += 1
            
            if y+1 <= len(M)-1:
                count_sum += M[y+1][x+1]
                count += 1
        
        if y-1 >= 0:
            count_sum += M[y-1][x]
            count += 1
        
        if y+1 <= len(M)-1:
            count_sum += M[y+1][x]
            count += 1
            
        return count_sum/count