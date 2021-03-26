from functools import cache
not_found = True
smallest_number = 2520

@cache
def is_divisible(num):
    tmp = num
    for i in range(1,21):
        if tmp % i != 0:
            return False
    return True


while not_found:
    if is_divisible(smallest_number):
        print(smallest_number)
        not_found = True
    smallest_number+=1

