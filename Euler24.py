
permutations = [];
count = 0;
def allPermutations(lst, value):

    if len(lst)==1:
        value+=lst[0];
        permutations.append(value);
        if len(permutations)==1000000:
            print(value);
    else:
        for i in lst:
            value+=i;

            temp = list(lst);
            temp.remove(i);

            allPermutations(temp, value);

            value = value[0:len(value)-1];

theList = ["0","1","2","3","4","5","6","7","8","9"];
allPermutations(theList, "");
