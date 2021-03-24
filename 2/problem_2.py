from functools import cache, lru_cache
#even fibonacci numbers



# remembers the values of the previus 
# computed function using cache

# lru_cache requires a specified size for the
# limit of previous computed function

@lru_cache(maxsize=2)
def fib_seq(terms):
    if terms <= 1:
        return terms
    else:
        return fib_seq(terms - 1) + fib_seq(terms - 2)
    
sum = 0
max = 4000000
fib = 0
i = 0
while fib < max:
    fib = fib_seq(i)
    if fib % 2 == 0:
        sum = sum + fib
    i = i + 1

    
print(sum)