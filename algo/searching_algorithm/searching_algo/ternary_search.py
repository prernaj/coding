'''
ternary search. 
given a sorted array.
in each range, brack the list into three parts with two mid indexes. check if item is at position mid1 or mid2.
then sent it to one of these three ranges.
'''

def ternary_search(arr, x, lo, hi):
    if hi < lo:
        return -1
    mid1 = int(lo + (hi-lo)/3)
    mid2 = int(mid1 + (hi-lo)/3)

    if arr[mid1] == x:
        return mid1

    if arr[mid2] == x:
        return mid2

    if arr[mid1] > x:
        hi = mid1 - 1
    elif arr[mid2] < x:
        lo = mid2 + 1
    else:
        lo = mid1 + 1
        hi = mid2 - 1
    return ternary_search(arr, x, lo, hi)

def main():
    arr = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
    x = 611
    n = len(arr)
    print ternary_search(arr, x, 0, n-1)

if __name__=='__main__':
    main()
