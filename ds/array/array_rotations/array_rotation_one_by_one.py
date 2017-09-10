'''
array rotation one by one - left_rotate(arr, d, n)
time : O(n*d)
space O(1)
'''
def rotate_left(arr, n, d):
    for i in range(0,d):
        first_elem = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first_elem

def main():
    arr = [1,2,3,4,5,6,7]
    n = 7
    d = 2
    rotate_left(arr, n, d)
    print 'output'
    for item in arr:
        print item,

if __name__ == '__main__':
    main()
