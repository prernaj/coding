'''
BA = R(ArBr)
A is arr(0:d)
B is arr(d:n)
'''
def reverse_array(arr, n):
    for i in range(0,n):
        j = n-i-1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]

def main():
    arr = [1,2,3,4,5,6,7]
    n = 7
    d = 2
    A = arr[0:d]
    reverse_array(A, d)
    B = arr[d:n]
    reverse_array(B, n-d)
    arr = A+B
    reverse_array(arr, 7)
    for item in arr:
        print item,

if __name__ == '__main__':
    main()
