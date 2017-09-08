'''
exponential search involves two steps:
1. find range where element in present
2. do binary search in above found range

how do we find range where element may be present ?
the idea is to start with subarray size 1 compare its last element with x, then try with size 2, then 4, and so on until last element of a subarray is not greater
once we find an inex i, we know that the element must be present between i/2 and i
'''

def exponential_search(arr, x, n, i, lo, hi):
    if hi < lo:
        return -1
    if arr[hi] == x:
        return hi
    lo = hi+1
    i = i * 2
    hi = lo + i 
    if hi >= n:
        hi = n-1
    if arr[hi] <= x:
        return exponential_search(arr, x, n, i, lo, hi)
    if arr[hi] > x:
        return binary_search(arr, x, i/2, hi)

def binary_search(arr, x, lo, hi):
    if hi < lo:
        return -1
    mid = int((lo+hi)/2)
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        hi = mid - 1
    else:
        lo = mid + 1
    return binary_search(arr, x, lo, hi)

def main():
    arr = [0,1,1,2,3,5,8,13,23,34,55,89,144,233,377,610]
    x = 2
    n = len(arr)
    print exponential_search(arr, x, n, 1, 0, 0)

if __name__=='__main__':
    main()

'''
Time complexity: O(logn)
Applications:
unbounded searches, where size of array is infinite.
it works bettwe than binary search for bounded arrays also when the elements to be searched is clser to the first element.
'''

