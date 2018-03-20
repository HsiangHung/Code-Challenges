# [#531] Lonely Pixel I
#
#  Using DFS will cost time complexity O(n*m*(m+n))
#
#  consider the property the lonely pixel happens if row and col index 
#  appears only ONCE.
#
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        Lcol = len(picture[0])
        Lrow = len(picture)
        
        row_dict, col_dict = {}, {}
        black_pixel = []
        for col in range(Lcol):
            for row in range(Lrow):
                if picture[row][col] == "B":
                    black_pixel.append((row, col))
                    row_dict[row] = row_dict.get(row, 0) + 1
                    col_dict[col] = col_dict.get(col, 0) + 1
        
        iso_black = 0
        for row, col in black_pixel:
            if row_dict[row] == 1 and col_dict[col] == 1:
                iso_black += 1
                    
        return iso_black