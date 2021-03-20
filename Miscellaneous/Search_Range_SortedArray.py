
'''

find the range of traget numbers in a sorted array

https://afteracademy.com/blog/search-for-a-range-in-sorted-array
https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

consider target number may not exist in the array
'''

def search_leftmost(arr, target):
    if len(arr) <= 2 and target not in arr: return -1

    if len(arr) == 1: return 0
    if len(arr) == 2: 
        return 1 if arr[0] != target else 0

    mid = len(arr) // 2

    if arr[mid] == target:
        if mid > 0 and arr[mid-1] < target: return mid
        idx = search_leftmost(arr[:mid], target)
        return idx if idx != -1 else -1 
    elif arr[mid] > target:
        idx = search_leftmost(arr[:mid], target)
        return idx if idx != -1 else -1 
    else:
        idx = search_leftmost(arr[mid+1:], target)
        return mid + 1 + idx if idx != -1 else -1


def search_rightmost(arr, target):
    if len(arr) <= 2 and target not in arr: return -1

    if len(arr) == 1: return 0
    if len(arr) == 2: 
        return 0 if arr[1] != target else 1

    mid = len(arr) // 2

    if arr[mid] == target:
        if mid < len(arr)-1 and arr[mid+1] > target: return mid
        idx = search_rightmost(arr[mid+1:], target)
        return mid + 1 + idx if idx != -1 else -1
    elif arr[mid] > target:
        idx = search_rightmost(arr[:mid], target)
        return idx if idx != -1 else -1
    else:
        idx = search_rightmost(arr[mid+1:], target)
        return mid + 1 + idx if idx != -1 else -1



def find_range(arr, target):

    leftmost, rightmost = linear_check(arr, target)
    print ("linear:", leftmost, rightmost)

    return search_leftmost(arr, target), search_rightmost(arr, target)

def linear_check(arr, target):

    leftmost, rightmost = None, None
    for i in range(len(arr)):
        if leftmost is None and arr[i] == target:
            leftmost = i
        
        if arr[i] == target:
            if i < len(arr) -1 and arr[i+1] != target: 
                rightmost = i
            elif i == len(arr) -1:
                rightmost = len(arr) -1

    return leftmost, rightmost


    
arr, target = [3, 3], 3

# arr, target = [3,3,3,3,3,5,7,8], 3

arr, target = [1, 3, 5, 5, 5, 5 ,28, 37, 42], 1

# arr, target = [5,7,7,8,8,10], 6
print (find_range(arr, target))