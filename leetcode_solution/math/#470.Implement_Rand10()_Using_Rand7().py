#  470. Implement Rand10() Using Rand7() (medium)
#  https://leetcode.com/problems/implement-rand10-using-rand7/
#
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    '''
    https://blog.csdn.net/Czyaun/article/details/103807816?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-2&spm=1001.2101.3001.4242
    '''
    def rand10(self):
        """
        :rtype: int
        """        
        while True:
            rand40 = (rand7() - 1) * 7 + rand7()
            if rand40 <= 40:
                return rand40 % 10 + 1
                
