# palindrome number of 2 3-digit products
from functools import cache
j = 10
i = 10

@cache
def calculate(i,j):
    return i*j

@cache
def palindrome(num):
    strnum = str(num)
    is_palindrome = True
    j = 0
    i = len(strnum) - 1
    while is_palindrome and j < len(strnum) and i >= 0:
        if strnum[i] != strnum[j]:
            return False
        j+=1
        i-=1
    return True

largest = 0
for i in range(999):
    for j in range(999):
        num = calculate(i,j)
        if palindrome(num):
            if largest < num:
                largest = num

print(largest)