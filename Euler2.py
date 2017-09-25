val_one = 1;
val_two = 2;
temp =0;
sum = 0;

while val_two<4000000:
        if (val_two % 2) ==0:
            sum+=val_two;
        else:
            sum+=0;

        temp = val_one+val_two;
        val_one = val_two;
        val_two = temp;


print(sum);
