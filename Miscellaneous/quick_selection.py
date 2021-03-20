'''
** Quick Selection ** 

find k-smallest element, help median value

https://www.geeksforgeeks.org/quickselect-algorithm/  (code source)
https://www.youtube.com/watch?v=BP7GCALO2v8 

the partition module comes from 
https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html 
which is easier to understand
'''

# def partition(arr, l, r):
#     x = arr[r]
#     i = l
#     for j in range(l, r):
#         if arr[j] <= x:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#     arr[i], arr[r] = arr[r], arr[i]
#     return i

def partition(arr, first, last):
    pivot = arr[first]
    L, R = first+1, last
    
    done = False
    while not done:

        while L <= R and arr[L] <= pivot:
            L += 1
            
        while L <= R and arr[R] >= pivot:
            R -= 1

        if R < L:
            done = True
        else:
            arr[L], arr[R] = arr[R], arr[L]

    arr[first], arr[R] = arr[R], arr[first]

    return R

def kthSmallest(arr, l, r, k):
 
    # if k is smaller than number of elements in array
    if k > 0 and k <= r - l + 1:
 
        # Partition the array around last element and get position of pivot element in sorted array
        index = partition(arr, l, r)
 
        if (index - l == k - 1): # if position is same as k
            return arr[index]
        elif (index - l > k - 1): # If position is more, recur for left subarray 
            return kthSmallest(arr, l, index - 1, k)
        else: # Else recur for right subarray 
            return kthSmallest(arr, index + 1, r, k - index + l - 1)

    return INT_MAX


arr = [ 10, 4, 5, 8, 6, 11, 26 ]
# arr = [35,33,42,10,14,19,27,44,26,31]
arr = [54,26,20,17,55,31,44,77]
n = len(arr)
k = 6
print(str(k)+"-th smallest element is ", end = "")
print(kthSmallest(arr, 0, n - 1, 5))
print (arr)
