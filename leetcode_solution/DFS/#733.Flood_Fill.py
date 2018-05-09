## [Leetcode#733] Flood Fill
##
##
cclass Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        self.DFS(image, sr, sc, oldColor)
        
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == -1:
                    image[row][col] = newColor
            
        return image
    
    def DFS(self, image, y, x, oldColor):
        
        if image[y][x] != oldColor:
            return
        
        image[y][x] = -1
        
        if y - 1 >= 0:
            self.DFS(image, y-1, x, oldColor)
            
        if y + 1 <= len(image)-1:
            self.DFS(image, y+1, x, oldColor)
            
        if x - 1 >= 0:
            self.DFS(image, y, x-1, oldColor)
            
        if x + 1 <= len(image[0])-1:
            self.DFS(image, y, x+1, oldColor)
            

                