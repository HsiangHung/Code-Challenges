## Binary Search
## return position index or return -1 if no target number exists
def BS(array, target, start):

    if len(array) == 1:
        if array[0] != target: return -1
        return start
          
    if len(array) == 2:
        if array[0] == target: return start
        if array[1] == target: return start+1
        return -1

    n = int(len(array)/2)
    half = array[start+n]
    
    if half == target:
         return half+start
    elif half > target:
         return BS(array[:n], target, start)
    elif half < target:
         return BS(array[n+1:], target, start+n+1)

    

print (BS([1,3,5,8,10,13], 0, 0))