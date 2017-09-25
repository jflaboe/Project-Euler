class Primes:

    def is_prime(self, num, update=True):
        if update is True:
            self._gen_primes_(num)
        
        for prime in self.primes:
            if prime >= num:
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

primes = Primes(100)

num = 5
found_answer = False
while found_answer is False:
    if primes.is_prime(num) is False:
        print(num)
        correct = False
        i = 1
        dub_square = 2*(i**2)
        while dub_square < num:
            if num - dub_square in primes.primes:
                correct = True
                break
            i += 1
            dub_square = 2*(i**2)
        
        if correct is False:
            print(num)
            break
        

    num += 2