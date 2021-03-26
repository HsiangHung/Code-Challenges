#  464. Can I Win (medium)
#  https://leetcode.com/problems/can-i-win/
#
class Solution:
    '''
    https://www.codenong.com/p12239515/
    https://blog.csdn.net/magicbean2/article/details/78581808
    
    我能保证赢的充分必要条件是：我选取了当前这个数字之后，对方无论如何都不可能赢”。
    如果我选择任何数字都不可能赢，那么对方就一定可以保证赢了
    
    DFS + memory
    '''
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        nums = [i for i in range(1, maxChoosableInteger+1)]
                
        if sum(nums) < desiredTotal:
            return False
        if sum(nums) == desiredTotal and len(nums) % 2 != 0:
            return True
        
        self.seen = {}
        return self.DFS(nums, desiredTotal)
    

    def DFS(self, nums, desiredTotal):      
        if desiredTotal <= nums[-1]:
            return True
        
        if tuple(nums) in self.seen: return self.seen[tuple(nums)]
        
        for i in range(len(nums)):
            if not self.DFS(nums[:i]+nums[i+1:], desiredTotal-nums[i]): 
                # here not is becuase to gaurantee win, make sure opponent not win.
                self.seen[tuple(nums)] = True
                return True
        
        self.seen[tuple(nums)] = False
        return False