def isPrime(x, primesArray):
    for i in primesArray:
        if x%i==0:
            return False;
    return True;

primes = [2,3];
primecount = 2;
num = 3;
while primecount<10001:
    num+=1;
    if isPrime(num,primes):
        primes.append(num);
        primecount = primecount+ 1;

print(primes.pop());
