#largest prime factor
NUM = 600851475143
largest = 0

def generate_primes(num):
    primes = []
    is_prime = [False,False] + [True] * (num-1)
    for p in range(2,num+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p,num+1,p):
                is_prime[i] = False
    return primes


print(max(generate_primes(NUM)))
