#sum square difference
MAX = 100

def square_sum(num):
    return (num*(num+1)/2)**2

def sum_of_squares(num):
    return (2*(num**3) + 3*(num**2) + num)/6

print(str(square_sum(100) - sum_of_squares(100)))