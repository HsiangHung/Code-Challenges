#  670. Maximum Swap (medium)
#  https://leetcode.com/problems/maximum-swap/
#
class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        Brutal force TC O(n!), but here we reduce to O(n^2)
        compare any two digits, if num[i] < num[j] for i < j, then swap can create a bigger number
        If the digits is montonically decreasing, no bigger number after a swap.
        e.g. num = 98368
        swap 3, 6 => 98638
        swap 3, 8 => 98863
        swap 6, 8 => 98386
        We see swap 3, 8 gives you answer
        '''
        max_num = num
        
        num = str(num)
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if num[i] < num[j]:
                    if j - i > 1:
                        new_num = num[:i] + num[j] + num[i+1:j] + num[i] # if switch index = 2, 5
                    else:
                        new_num = num[:i] + num[j] + num[i]  # if swith index = 2, 3
                        
                    if j < len(num) - 1:
                        new_num += num[j+1:] # if j is not the last number
                   
                    max_num = max(int(new_num), max_num)
                
        return max_num
        