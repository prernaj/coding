'''
BA = R(ArBr)
A is arr(0:d)
B is arr(d:n)
'''
def reverse_array(arr, a, b):
    for i in range(a, b):
        j = b-i-1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]

def rotate_left(arr, n, d):
    reverse_array(arr, 0, d)
    reverse_array(arr, d, n)
    reverse_array(arr, 0, n)

def main():
    arr = [1,2,3,4,5,6,7]
    n = 7
    d = 2
    rotate_left(arr, n, d)
    for item in arr:
        print item,

if __name__ == '__main__':
    main()
