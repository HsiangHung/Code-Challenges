
# Algorithms: sorting

## Bubble Sort
```Python
# Bubble: O(n^2)
def bubbleSort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        jj = arr_len-1
        for j in range(jj):
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
        jj -= 1
    return arr
    
arr = [4, 54, 26, 93, 17, 77, 31, 44, 1, 0]      
print (bubbleSort(arr))
```

##  Selection Sort
```Python
## Selection sort: O(n^2)
def selectionSort(arr):
    arr_len = len(arr)
    jj = arr_len
    for i in range(arr_len):
        max_arr = float('-infinity')
        for j in range(jj):
            if arr[j] > max_arr:
                max_arr = arr[j]
                max_site = j
        print (max_arr, max_site)
        arr[max_site], arr[jj-1] = arr[jj-1], arr[max_site]
        jj -= 1
    return arr
    
arr = [4, 54, 26, 93, 17, 77, 31, 44, 1, 0]      
print (selectionSort(arr))
```

## Insertion Sort
```Python
## Insertion sort: O(n^2)
def insertionSort(arr):
    arr_len = len(arr)
    subArr = [arr[0]]
    arr.pop(0)
    for i in range(arr_len-1):
        #print (i, len(subArr))
        isInsert = False
        for j in range(len(subArr)):
            if subArr[j] > arr[0]:
                #print (j, subArr[j], arr[0])
                subArr.insert(j, arr[0])
                arr.pop(0)
                isInsert = True
                break  ## Note!! this break is super important !!!!
        if isInsert == False: 
            subArr.append(arr[0])
            arr.pop(0)
        print (len(subArr), subArr, arr)
    return subArr
            
arr = [4, 54, 26, 93, 17, 77, 31, 44, 1, 0]      
print (insertionSort(arr))
```

## Merge Sort
```Python
## Merge Sort: O(n*logn)
def mergeSort(arr):
    arr_len = len(arr)
    if arr_len <= 1: return arr
    left = arr[:int(arr_len/2)]
    right = arr[int(arr_len/2):]
    print (left,right)
    left = mergeSort(left)
    right = mergeSort(right)
    #print ('----')
    return insertionSort(left+right)
    
    
arr = [54, 26, 93, 17, 77, 31, 44, 1, 0]      
print(mergeSort(arr))
````






