## [Greek] Maximum Index
#
#  Given an array arr[], find the maximum j – i such that arr[j] > arr[i].
#
# Examples:
#
#  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
#  Output: 6  (j = 7, i = 1)
#
def maxIndexDiff(arr):

    LMin, RMax = [], []
    
    LMin.append(arr[0])
    for i in range(1, len(arr)):
        LMin.append(min(arr[i], LMin[i-1]))
 
    RMax.append(arr[-1])
    for j in range(len(arr)-2, -1, -1):
        RMax.insert(0, max(arr[j], RMax[0]))
        
        
    print (LMin, RMax)
    
    
    i, j, maxDiff = 0, 0, -1;
    while j < len(arr) and i < len(arr):
        if LMin[i] < RMax[j]:
            maxDiff = max(maxDiff, j-i);
            j += 1
        else:
            i += 1
            
        print (i,j, maxDiff)
   
    return maxDiff;
    
    
arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]

#arr =  [6, 5, 4, 3, 2, 1]

print (maxIndexDiff(arr))
        