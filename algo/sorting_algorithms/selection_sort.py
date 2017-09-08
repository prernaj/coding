'''
the selction sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
the algorithm maintains two subarrays in a given array.
1. the subarray which is already sorted.
2. remaining subarray which is unsorted.
in each iteration of selction sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

'''
def selection_sort(arr, n, ind):
    if ind >= n:
        return arr
    elem = arr[ind]
    for i in range(0, ind):
        print elem, arr[i]
        if elem < arr[i]:
            for j in range(ind, i, -1):
                arr[j] = arr[j-1]
            arr[i] = elem
            break
    return selection_sort(arr, n, ind+1)

def main():
    arr = [64, 25, 12, 22, 11]
    n = len(arr)
    print selection_sort(arr, n, 0)

if __name__ == '__main__':
    main()

'''
time complexity: O(n*n) 
the good thing about selection sort is that it never makes more than O(n) swaps and can be useful when memor writes is a costly operation.
'''
