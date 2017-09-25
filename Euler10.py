def isPrime(x,primes):
    for i in primes:
        if x%i ==0:
            return False;
    return True;


primelist = [2,3]
sum = 5;
a = 3;
while a<2000000:
    a+=2;
    print(a);
    if isPrime(a,primelist):
        primelist.append(a);
        sum+=a;

print(sum);
