import math

def is_prime(num):
    if num == 2 or num ==3:
        return True
    if num%2==0:
        return False
    
    for i in range(3, int(math.sqrt(num)+2),2):
        if num%i==0:
            return False
    return True


def prime_factorize(num):
    if num==0:
        return[0]
    if is_prime(num):
        return [num]
    
    count = 2
    while count <= math.sqrt(num):
        if num%count == 0:
            return prime_factorize(count) + prime_factorize(int(num/count))
        count+=1

    print(num)
    

def list_mult(l):
    prod = 1
    for num in l:
        prod*=num
    return prod

factors_list = []
for i in range(2,6):
    factors_list.append(len(list(set(prime_factorize(i)))))

i = 6
no_answer = True
while no_answer is True:
    factors_list.pop(0)
    factors_list.append(len(list(set(prime_factorize(i)))))
    
    all_four = True
    for length in factors_list:
        if length < 4:
            all_four = False
            break
    if all_four == True:
        print(i-3)
    
    i += 1