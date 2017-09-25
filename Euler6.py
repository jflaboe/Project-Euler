square_sum = 0;
sum = 0;

for i in range(0,101):
    sum+=i;
    square_sum+=i**2;
print(sum**2-square_sum);
