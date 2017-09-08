'''
given an array arr[] of n elements, write a function to search a given element x in arr[].
'''

def search(arr, x):
    for item in arr:
        if item == x:
            return arr.index(x)
    return -1

def main():
    arr = [1,2,3,4,5]
    x = 4
    print search(arr,x)

if __name__=='__main__':
    main()


'''
Time complexity: O(1)
'''
