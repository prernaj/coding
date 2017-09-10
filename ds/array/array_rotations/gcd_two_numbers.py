'''
GCD Greatest common divisor is the largest number that divides the given numbers
1. find the divisors of a given number
2. find the greatest number that these lists have in common.
Euclidean algorithm is the main algorithm uses for this purpose.
Based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.
GCD of 252 and 105 = GCD of 147 and 105 = GCD of 42 and 105 = GCD of 42 and 63 = GCD of 42 and 21 = GCD of 21 and 21 = 21
'''

def gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == num2:
        return num1
    elif num1 > num2:
        diff = num1-num2
        return gcd(diff, num2)
    else:
        diff = num2-num1
        return gcd(num1, diff)

def main():
    num1 = 2
    num2 = 1
    ans = gcd(num1, num2)
    print 'GCD of {0} and {1} is {3}'.format(num1, num2, ans)

if __name__ == '__main__':
    main()
