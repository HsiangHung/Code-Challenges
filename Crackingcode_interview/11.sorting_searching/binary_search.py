## Binary Search
## return position index or return -1 if no target number exists
def binary_search(offset, nums, target):
    if len(nums) == 0:
        return -1
    
    if len(nums) == 1:
        if target != nums[0]:
            return -1
        else:
            return offset
        
    middle = len(nums)//2
    if nums[middle] == target:
        return offset+middle
    elif nums[middle] > target:
        return binary_search(offset, nums[:middle] , target)
    elif nums[middle] < target:
        return binary_search(offset+middle+1, nums[middle+1:], target)
    
    
print (binary_search(0, [0, 1, 2, 8, 13, 17, 19, 32, 42], 19))