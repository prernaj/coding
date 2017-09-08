'''
jump search is for sorted array.
the basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
for example:
    suppose we have an array arr of size n and blcok to be jumped size m. then we search at the indices arr[0], arr[m], arr[2m]... arr[km] and so on.
    once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation from the index km to find the element x.
arr = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610). n = 16.
jump search will find the value of 55 with the following stpes assuming that the block size to be jumped is 4.
step 1: jump 0 to 4
step 2: jump 4 to 8
step 3: jump 8 to 12
since the elemnt at index 12 is greater than 55, we will jump back to a stpe and start linear search from index 9.

what is the optimal block size to be skipped ?
in the worst case we have to do n/m jumps an if the last checked value is greater than the element to be searched for, we perform m-1 comparisons more for linear search.
therefore the toal number fo comparisons is n/m + m-1.
the value of the function n/m + m-1 will be minimum when m = sqrt(n)
therefore the best step size is m = sqrt(n)
'''
import math

def jump_search(arr, n, m, x, lo, hi):
    if hi < lo:
        return -1
    if hi >= n or (hi < n and arr[hi] >= x):
        return lo
    else:
        lo = hi + 1
        hi = hi + m
        return jump_search(arr, n, m, x, lo, hi)

def jump_search_main(arr, n, m, x, lo, hi):
    ind = jump_search(arr, n, m, x, lo, hi)
    if ind == -1:
        return -1
    elif arr[ind] == x:
        return ind
    else:
        for i in range(ind+1, ind+m-1):
            if arr[i] == x:
                return i
        return -1


def main():
    arr = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
    x = 1
    n = len(arr)
    m = int(math.sqrt(n))
    print jump_search_main(arr, n, m, x, 0, m)

if __name__=='__main__':
    main()

'''
Time complexity = O(sqrt(n))
'''



