# Binary search for arr[i] < target but arr[i+1] >= target:


# Option 1: recrusion
# slow. When running recusion, sliding arr[:mid] or arr[mid:] takes time complexity O(n)

def search1(target, arr):
    """
    This func looks for index where arr[i] < target but arr[i+1] >= target

    Time complexity O(n)
    """
    if arr[0] >= target:
        return 0
    elif arr[-1] < target:
        return -1 
    
    mid = len(arr) // 2
    if arr[mid-1] < target and arr[mid] >= target:
        return mid
    elif arr[mid] < target:
        res = search1(target, arr[mid:])
        return res + mid if res != -1 else -1
    else:
        res = search1(target, arr[:mid])
        return res if res != -1 else -1



# Option 2: Iterative
# fast. Using two pointer l, r to graudally approach i

def search2(target, arr):
    """
    This func looks for index where arr[i] < target but arr[i+1] >= target

    Time complexity O(log n)
    """
    if arr[0] >= target:
        return 0
    elif arr[-1] < target:
        return -1 

    l, r = 0, len(arr)-1

    # there must be a soution found; otherwise at the beginning it will return
    while l <= r:
        mid = (r + l) // 2
        if arr[mid-1] < target and arr[mid] >= target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1


if __name__ == "__main__":

    arr = [0,1,3,4,5,8,10,12,50]
    print(search2(6, arr))
    print(search2(-1, arr))
    print(search2(3, arr))
    print(search2(100, arr))