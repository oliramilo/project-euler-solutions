#largest prime factor
import math
from functools import cache
NUM = 600851475143
largest = 0

def is_prime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True
 


done = False
i = 29
max_prime_num = i
while i < math.floor((NUM/4)):
    if is_prime(i):
        max_prime_num=i
        print(max_prime_num)
    i+=1

print(max_prime_num)