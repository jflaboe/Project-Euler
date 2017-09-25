def ispalindrome(x):
    word = str(x);
    length = len(word);

    i=0;
    while i < length/2:
        if word[i:i+1]!=word[length-1-i:length-i]:
            return False;

        i+=1;
    return True;

ispalindrome(101);
ispalindrome(201);
max = 0;
for i in range(100,1000):
    for j in range(100,1000):
        if ispalindrome(i*j):
            if i*j> max:
                max = i*j;
print(max);

bool = True;

for x in range(1,21):
    if (58198140*4)%x !=0:
        print(x);

print(58198140*4);
