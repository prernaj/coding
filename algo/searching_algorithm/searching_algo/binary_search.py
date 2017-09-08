'''
given a sorted arr of n elements, write a funciton to search a given element x in arr
'''
'''
binary search: search a sorted array by repeatedly dividing the search interval in half.
begin with an interval covering the whole array.
if the value of the search key is less than the item in the middle of the interval, narrow the interval to lower half. 
otherwise narrow it to upper half.
repeatedly check until the value is found or the interval is empty.
'''
def binary_search(arr, x, start, end):
    if start > end:
        return -1
    mid = int((end+start)/2)
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        start = mid+1
    else:
        end = mid-1
    return binary_search(arr, x, start, end)

def main():
    arr = [1,2,3,4,5]
    x = 1
    n = len(arr)
    print binary_search(arr, x, 0, n-1)

if __name__=='__main__':
    main()

'''
Time complexity: O(logn)
'''
