from itertools import permutations
class Primes:

    def is_prime(self, num, update=True):
        if update is True:
            self._gen_primes_(num)
        
        for prime in self.primes:
            if prime >= num**(0.5):
                return True
            if num % prime == 0:
                return False
        return True

            

    def _gen_primes_(self, max_val):
        if max_val > self.max_val:
            i = self.max_val
            while i < max_val:
                i += 1
                if self.is_prime(i, update=False) is True:
                    self.primes.append(i)
            self.max_val = max_val
                



    def __init__(self, max_val):
        self.primes = [2,3]
        self.max_val = 3
        self._gen_primes_(max_val)

primes = Primes(10000)


testable = []
for prime in primes.primes:
    if prime > 1000:
        testable.append(prime)

for prime in testable:
    perms = [int(''.join(p)) for p in permutations(str(prime))]
    perms = list(set(perms))
    perms.sort()
    acceptable = []
    for perm in perms:
        if primes.is_prime(perm):
            acceptable.append(perm)
    if len(acceptable) > 2:
        for i in range(0, len(acceptable)-2):
            for j in range(i + 1, len(acceptable)-1):
                for k in range(j + 1, len(acceptable)):
                    if acceptable[j]-acceptable[i] == acceptable[k]-acceptable[j]:
                        print(str(acceptable[i]) + str(acceptable[j]) + str(acceptable[k]))