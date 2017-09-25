def perform(n):
    if n%2 == 0:
        return n/2;
    else:
        return 3*n+1;

max_chain = 0;
chain = 0;
max_num= 0;


for i in range(1,1000000):
    print(i);
    n=i;
    chain = 1;
    while n!=1:
        n = perform(n);
        chain +=1;
    if chain>max_chain:
        max_chain = chain;
        max_num = i;
print(max_num);
