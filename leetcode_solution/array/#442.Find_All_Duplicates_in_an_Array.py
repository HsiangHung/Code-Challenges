# [# 442] Find All Duplicates in an Array
#  
#  Poket games
#
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # http://bookshadow.com/weblog/2016/10/25/leetcode-find-all-duplicates-in-an-array/
        # through all nums, take the number as the index |n|, 
        # if nums[|n|-1] > 0 => first appear, nums[|n|-1] = -nums[|n|-1]
        # if nums[|n|-1] < 0 => second appear, store nums[|n|-1] 
        # num = 4, [4,3,2,7,8,2,3,1]    => [4,3,2,-7,8,2,3,1]
        # num = 3, [4,3,2,-7,8,2,3,1]   => [4,3,-2,-7,8,2,3,1]
        # num =-2, [4,3,-2,-7,8,2,3,1]  => [4,-3,-2,-7,8,2,3,1]
        # num =-7, [4,-3,-2,-7,8,2,3,1] => [4,-3,-2,-7,8,2,-3,1] 
        # num = 8, [4,-3,-2,-7,8,2,-3,1] =>[4,-3,-2,-7,8,2,-3,-1]
        # num = 2, we have nums[2-1] = -3, so -3 repeat
        # num =-3, we have nums[|-3|-1] = -2, so -2 repeat
        # nums=-1, [4,-3,-2,-7,8,2,-3,-1] => [-4,-3,-2,-7,8,2,-3,-1]
        
        duplicated_nums = []
        for i in range(len(nums)):
            num = nums[abs(nums[i])-1]
            if num < 0:
                duplicated_nums.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -num
        
        return duplicated_nums
        
        
    def hashTable(self, nums):
        '''Hash table method, easy. time O(n) but space O(n)'''
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            
        return [num for num in num_dict if num_dict[num] > 1]
        
    def SortandSearch(self, nums):
        '''This use bubble sorts and then check if nums[i] == nums[i+1]
           but this method results to exceed limit time. time O(n^2)
        '''
        isSorted = False
        site = 1
        while not isSorted:
            isSorted = True
            for i in range(len(nums)-site):
                if nums[i] > nums[i+1]:
                    isSorted = isSorted and False 
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        
            site += 1
            
        duplicated_nums = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                duplicated_nums.append(nums[i])
            
        return duplicated_nums
        