'''
a function rotate(arr, d, n) that rotates arr of size n by d elements
Method 1: rotate_using_temp_array() time O(n) Space O(d)
'''

def rotate_using_temp_array(arr, d, n):
    temp_arr = []
    for i in range(0, d):
        temp_arr.append(arr[i])
    for i in range(d, n):
        arr[i-d] = arr[i]
    for i in range(0, d):
        arr[n-d+i] = temp_arr[i]

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = 7
    d = 5
    if d > n:
        print 'Stpes is gretaer than size of array'
        return
    output = rotate_using_temp_array(arr, d, n)
    print 'output'
    for item in arr:
        print item,


if __name__ == '__main__':
    main()
