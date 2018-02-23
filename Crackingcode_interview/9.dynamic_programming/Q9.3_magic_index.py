## Q9.3: magic index A[i] = i
##
#
# if the array is an ordered distinct list
def magic_index(offset, nums):
    if len(nums) == 0: return -1
    if len(nums) == 1:
        if nums[0] != offset:
            return -1
        else:
            return offset
    
    middle = len(nums)//2
    print (offset, middle+offset, nums[middle])
    if nums[middle] == middle+offset:
        return nums[middle]
    elif nums[middle] < middle:
        return magic_index(middle+offset+1, nums[middle+1:])
    else:
        return magic_index(offset, nums[:middle])
    
    

a = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12]
print (magic_index(0, a))

