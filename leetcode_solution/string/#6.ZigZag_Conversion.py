# [#6] ZigZag Conversion
#
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # e.g. s = "PAYPALISHIRING", numRows = 4
        # i for every int = (2*(numRows-2) + 1)+1 perid will appear first row
        # and then i-j and i+j, where j = 1,2,..int//2    
        
        if numRows == 1: return s
        if len(s) < numRows: return s
        
        interval = (2*(numRows-2)+1)+1
        
        read= ''
        for j in range(0, interval//2 +1):
            for i in range(0, len(s)+j, interval):
                ## note here len(s) + j "+j" is important since it considers missing strings.
                if j == 0:
                    read += s[i]
                elif interval/2 > j > 0:
                    if i == 0:
                        read += s[i+j]
                    elif i+j >= len(s):
                        read += s[i-j]
                    else:
                        read += s[i-j] + s[i+j]
                elif j == interval/2:
                    if i+j < len(s):
                        read += s[i+j]
            
        return read
        