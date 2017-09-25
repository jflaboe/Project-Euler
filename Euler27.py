def isPrime(num):
    if num<2:
        return False;
    if num ==2:
        return True;
    if num ==3:
        return True;


    limit = num**(1/2.0);

    i = 1;
    while i<limit:
        i+=2;
        if num%i == 0:
            return False;
    return True;


def f(a, b, n):
    return n**2 + a*n + b;

max_primes = 0;
product = 0;
run = True;
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0;
        run = True;
        while run:
            if isPrime(f(a,b,n)):
                n+=1;
            else:
                run = False;

        if n>max_primes:
            max_primes = n;
            product = a*b;

print(product);
