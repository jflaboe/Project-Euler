from itertools import permutations

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

primes = Primes(1000000)

for prime in primes.primes:
    

    for changes in range(1, len(str(prime))):
        
        perm_string = (len(str(prime))-changes)* "a" + changes*"*"
        
        
        perms = [''.join(p) for p in permutations(perm_string)]
        perms = list(set(perms))
        for perm in perms:
            perm_list = []
            prime_string = str(prime)
            
            for loc in range(0, len(perm)):
                if perm[loc] == "*":
                    perm_list.append(loc)
            
            
            prime_list = []
            start = 0
            if 0 in perm_list:
                start = 1
            
            for num in range(start,10):
                for loc in perm_list:
                    prime_string = prime_string[:loc] + str(num) + prime_string[loc+1:]
                
               
                if primes.is_prime(int(prime_string)):
                    prime_list.append(int(prime_string))
            if len(prime_list) > 7:
                print(prime_list)
