import math
from itertools import permutations
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

perms_string = '987654321'
found_prime = False
for j in range(0,9):
    
    if found_prime is True:
        break
    
    print(perms_string)
    perms = [''.join(p) for p in permutations(perms_string)]
    perms.sort()
    primes = list_of_primes(int(math.sqrt(int(perms_string))))
    print(perms_string)

    for i in range(0, len(perms)):
        cur = perms[len(perms)-1-i]
        if is_prime(int(cur), primes):
            print(cur)
            found_prime = True
            break
    perms_string = perms_string[1:]