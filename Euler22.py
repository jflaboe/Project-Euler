f = open("names.txt",'r');

text = f.read();
recording = False;
name = "";
names = [];
for i in text:

    if i =="\"":
        if recording:
            recording = False;
            names.append(name);
            name = "";
        else:
            recording = True;
    else:
        if recording:
            name+=i;
names.sort();
def nameScore(word):
    sum = 0;
    for i in word:
        sum = sum + ord(i)-64;
    return sum;

length = len(names);
sum = 0;
for j in range(0,length):
    sum = sum + ((1 + j) * nameScore(names[j]));
print(sum);
