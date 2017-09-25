def numDivisors(x):
    numDiv = 1;
    i = 2;
    while i < x**(1/2.0):
        if x%i==0:
            numDiv+=2;
        i+=1;
    return numDiv;

sum = 0;
num = 0;
bool = True;
max_divisors = 0;
while bool:
    sum = sum + num;
    num+=1;
    z = numDivisors(sum);
    if z > max_divisors:
        max_divisors = z;
        print(z);
    if max_divisors>500:
        bool = False;
        print(sum);
