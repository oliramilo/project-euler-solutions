#multiples of 3 and 5 problem

def get_sum_multiples(val):
    sum = 0
    if val > 1:
        for i in range(1,val):
            if i % 5 == 0 or i % 3 == 0:
                sum = sum + i
        return sum
    else:
        return 0

print('Enter Maximum value');
val = int(input())
print(get_sum_multiples(val))