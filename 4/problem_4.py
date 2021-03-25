# palindrome number of 2 3-digit products
import math

def calculate(i,j):
    return i*j

def palindrome(num):
    if num <= 0:
        return num == 0
    # number of digits of num
    dgt_size = math.floor(math.log(num,10)) + 1
    # let msd be the most significant digit of num
    msd = 10**(dgt_size - 1)
    for i in range(dgt_size // 2):
        if num // msd != num % 10:
            return False
        num %= msd # Remove the most significant digit of num
        num //= 10 # Remove the least significant digit of num
        msd //= 100 
    return True

largest = 0
for i in range(10,999):
    for j in range(10,999):
        num = calculate(i,j)
        if palindrome(num):
            if largest < num:
                largest = num

print(largest)