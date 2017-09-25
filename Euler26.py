def divide(num, den, num_iter):

    count = 0
    result = ""
    while count < num_iter:
        if num < den:
            num = num*10
        
        result += str(int(num/den))
        num = num - int(num/den)*den
        count += 1
    return result

def search_sequence(sequence):

    for i in range(1, int(len(sequence)/2)):

        repeat = sequence[0:i]
        

        test_sequence = sequence[:len(sequence) - len(sequence) % len(repeat)]
        test_sequence = test_sequence.replace(repeat, "")

        

        if len(test_sequence) == 0:
            return repeat

divide(1,999,1000)

max_d = 0

max_len = 0

for i in range(1, 1000):
    
    new_repeat = search_sequence(divide(1,i,100+i*3)[25:])
    if not new_repeat is None:
        if len(new_repeat) > max_len:
            max_len = len(new_repeat)
            max_d = i
    else:
        print(i)

print("best is " + str(max_d))
print(max_len)
    
        

