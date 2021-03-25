#largest prime factor
NUM = 600851475143
largest = 0

def gcd(x,y):
    print(x)
    if x == 0:
        return y
    return gcd(y, x % y)


