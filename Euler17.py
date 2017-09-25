numbers = {"0":0,"1":3,"2":3,"3":5,"4":4,"5":4,"6":3,"7":5,"8":5,"9":4, "10":3, "11":6,"12":6,"13":8,"14":8,"15":7,"16":7,"17":9,"18":8,"19":8,"20":6,"30":6,"40":5,"50":5,"60":5,"70":7,"80":6,"90":6};

sum = 0;
for i in range(1,1000):
    word = str(i);
    if len(word)==1:
        sum+=numbers[word];
    if len(word)==2:
        if word[0] == "1":
            sum+=numbers[word];
        else:
            sum+=numbers[str(10*int(word[0]))];
            sum+=numbers[word[1]];
    if len(word)==3:
        sum+=numbers[word[0]];
        sum+=7;
        if int(word)%100!=0:
            sum+=3;

        if word[1] == "1":
            sum+=numbers[word[1:3]];
        else:
            sum+=numbers[str(10*int(word[1]))];
            sum+=numbers[word[2]];
sum+=11;

print(sum);
