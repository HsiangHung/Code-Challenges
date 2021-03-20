'''

** QUick Sort **

https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm
https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html (code source)
https://www.youtube.com/watch?v=SLauY6PpjW4

O(nlogn), worst O(n^2)

Step 1 − Choose the highest index value has pivot
Step 2 − Take two variables to point left and right of the list excluding pivot
Step 3 − left points to the low index
Step 4 − right points to the high
Step 5 − while value at left <= pivot move right
Step 6 − while value at right >= pivot move left
Step 7 − if both step 5 and step 6 does not match, swap left <=> right
Step 8 − if left > right, the point where they met is new pivot
'''


def quickSort(arr, first, last):
   if first < last:
       splitpoint = partition(arr, first, last)
       quickSort(arr, first, splitpoint-1)
       quickSort(arr, splitpoint+1, last)

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


# def partition(arr, low, high):
#     i = low -1        # index of smaller element 
#     pivot = arr[high]     # pivot   
#     for j in range(low, high): 
#         if arr[j] <= pivot: 
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i] 
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1) 


arr = [54,26,20,17,55,31,44,77]
# arr = [6,3,1,8,5,2,7,9,15]
# arr = [35,33,42,10,14,19,27,44,26,31]
arr = [3,2,1,5,6,4]
quickSort(arr, 0, len(arr)-1)
print(arr)

        
        

