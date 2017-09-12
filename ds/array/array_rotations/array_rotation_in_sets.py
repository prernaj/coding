'''
jugling algorithm for array rotation
instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d
and move elemtns within the sets.
'''
from gcd_two_numbers import gcd

def rotate_array_in_sets(arr, n, d):
    g = gcd(n, d)
    for i in range(0, g):
        temp = arr[i]
        j = i
        while True:
            k = j+d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def main():
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = 12
    d = 7
    rotate_array_in_sets(arr, n, d)
    for item in arr:
        print item,

if __name__ == '__main__':
    main()
