## Binary Search for lower bound
#
#   if -1, means, the target is even smaller than the lowest value of array
#   then the lower bound index. e.g. arr = [1,2,4]
#   if target = 3, then gives 1 since arr[1] <= target < arr[2]
#
def BS_lowerBound(arr, target):
  	'''binary search for lower bound '''      
    if len(arr) == 1:
        if arr[0] <= target: return 0
        return -1
 
    if len(arr) == 2:
        if arr[0] <= target < arr[1]: return 0
        if arr[1] <= target: return 1
        return -1
                
    mid = len(arr) // 2 
        
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BS_lowerBound(arr[:mid], target)
    elif arr[mid] < target:
        return mid+1+BS_lowerBound(arr[mid+1:], target)
            
        

arr = [0,1,3,4,5,8,10,12,50]
for x in arr:
    print (x, BS_lowerBound(arr, x))
    
print ()
print (-5, BS_lowerBound(arr, -5))
print (2, BS_lowerBound(arr, 2))
print (7, BS_lowerBound(arr, 7))
print (9, BS_lowerBound(arr, 9))
print (11, BS_lowerBound(arr, 11))
print (13, BS_lowerBound(arr, 13))
print (20, BS_lowerBound(arr, 20))
print (60, BS_lowerBound(arr, 60))