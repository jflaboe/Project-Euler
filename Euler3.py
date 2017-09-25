def isprime(a):
    if a<2:
        return False;
    if a%2 == 0:
        return False;

    i = 3;
    while i<(a**(1/2.0)):
        if a%i==0:
            return False;
        i = i+2;
    return True;

print(isprime(5));
print(isprime(17));
print(isprime(20));
print(isprime(6857));


def largest_prime(x):
    largest_prime = 3
    j = 2;
    while j < x**(1/2.0):
        if x%j ==0:
            if isprime(j):
                if j>largest_prime:
                    largest_prime=j;
            if isprime(x/j):
                if (x/j)>largest_prime:
                    largest_prime = j;
        j = j +1;
    return largest_prime;

print(largest_prime(600851475143));
