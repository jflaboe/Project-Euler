def d(n):
    sum = 1;
    i = 1;
    while i< n**(1/2.0):
        i+=1;
        if n%i==0:
            sum = sum+i+(n/i);
    return sum;
count = 0;

for j in range(0,10000):
    if d(j)!=j and d(j)<10000:
        if d(d(j))==j:
            count+=j;

print(count);
