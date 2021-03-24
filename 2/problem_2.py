#even fibonacci numbers


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