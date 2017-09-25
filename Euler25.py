index = 3;
F1 = 1;
F2 = 2;
length = 1;
while length<1000:
    index+=1;
    temp = F1 + F2;
    F1 = F2;
    F2 = temp;
    length = len(str(F2));

print(index);
