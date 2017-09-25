

class Primes:

    def is_prime(self, num, update=True):
        if update is True:
            self._gen_primes_(num)
        
        for prime in self.primes:
            if prime >= num**(0.5)+1:
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

total = 0
i = 0
while total < 1000000:
    total = total + primes.primes[i]
    i = i + 1

new_primes = primes.primes[0:i]

max_chain = len(new_primes)
chain = max_chain

not_found = True
while not_found is True:
    start = 0
    while start <= max_chain - chain:
        total = sum(new_primes[start:start+chain])
        if primes.is_prime(total):
            print(total)
            not_found = False
            break
        start = start + 1
    chain = chain - 1