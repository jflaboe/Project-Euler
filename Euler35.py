import math
def list_of_primes(max_prime):
    if max_prime < 2:
        return []
    primes = [2]

    for i in range(3,max_prime+1):
        is_prime = True
        square = math.sqrt(i)
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            elif prime > square:
                break
        if is_prime is True:
            primes.append(i)
    return primes

def is_prime(num, prime_list):
    square = math.sqrt(num)
    for prime in primes:
        if num % prime ==0:
            return False
        elif prime > square:
            return True
    return True

primes = list_of_primes(1000000)
print("created list")
def circular_primes(num, prime_list):
    num = str(num)
    primes = []
    for i in range(0,len(num)):
        if not int(num) in prime_list:
            return []
        primes.append(int(num))
        num = num[1:] + num[0]
    return primes

circulars = []

for prime in primes:
    if prime in circulars:
        pass
    else:
        circulars = circulars  + circular_primes(prime, primes)
print(list(set(circulars)))
print(len(list(set(circulars))))
