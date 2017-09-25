fact = 1;
for i in range(1,101):
    fact = fact*i;


word = str(fact);
sum = 0;
for j in word:
    sum+=int(j);

print(sum);
