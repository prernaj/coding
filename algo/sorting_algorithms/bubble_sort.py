'''
bubbl sort.
repeatedly swappng the adjacent elements if they are in wrong order.
the algorithm needs one whole pass without any swap to know it is sorted.
'''

def bubble_sort(arr, n):
    flag = True
    while flag:
        swapped = False
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
                swapped = True
        if swapped == False:
            flag = False
    return arr
    

def main():
    arr = [5,1,4,2,8]
    n = len(arr)
    print bubble_sort(arr, n)

if __name__=='__main__':
    main()

'''
time complexity: O(n*n). when array is reversed sorted
best case: O(n) when array is already sorted.
'''
