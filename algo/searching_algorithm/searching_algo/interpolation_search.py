'''
given a sorted array of uniformly distributed values arr[], write a function to search for a particular element x in the array.
the interpolation search is an improvement over binary search for instances, where the values in a sorted array are uniformly distributed.
binary search always goes to middle element to check.
on the other hand interpolation search may go to different location according to value of key being searched.
for example, if the value of key is closer to the last element, interpolation search is likely to start search toward the end side.
to find the position to be searched, it uses following formula
The idea of formula is to return higher value of pos when element to be searched is closer to arr[hi] and smaller value when closer to arr[lo]
pos = lo + [(x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo])]
'''

def interpolation_search(arr, n, x, lo, hi):
    if hi < lo or arr[lo] > x or arr[hi] > x:
        return -1
    pos = int(lo + ((x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo])))
    if pos > 0 and pos < n and arr[pos] == x:
        return pos
    if pos > 0 and pos < n and arr[pos] > x:
        hi = pos - 1
    else:
        lo = pos + 1
    return interpolation_search(arr, n, x, lo, hi)

def main():
    arr = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
    x = 140
    n = len(arr)
    print interpolation_search(arr, n, x, 0, n-1)

if __name__=='__main__':
    main()

'''
Time complexity: if elements are uniformly distributed O(loglogn).
in worst case upto O(n)
'''
