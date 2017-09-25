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

def reduce_frac(num, den):
    num_prime = prime_factorize(num)
    den_prime = prime_factorize(den)

    num_count = 0
    den_count = 0

    while num_count < len(num_prime) and den_count < len(den_prime):
        if num_prime[num_count]==den_prime[den_count]:
            num_prime.pop(num_count)
            den_prime.pop(den_count)
        elif num_prime[num_count] < den_prime[den_count]:
            num_count = num_count + 1
        else:
            den_count = den_count + 1
    try:
        result = (list_mult(num_prime), list_mult(den_prime))
        return result
    except:
        return (0,1)

def improper_reduce(num, den):
    num = str(num)
    den = str(den)
    for i in range(0,len(num)):
        if num[i] in den:
            denpos = den.find(num[i])
            den = den[0:denpos] + "*" +den[denpos+1:]
            num = num[0:i] + "*"+num[i+1:]
    try:

        return (int(num.replace("*", '')), int(den.replace("*", '')))
    except:
        return (0,1)


for num in range(10,99):
    for den in range(num+1,100):
        num2, den2 = improper_reduce(num,den)
        
        if (num2,den2) == (num,den):
            pass
        elif num%10 ==0:
            pass
        else:
            if reduce_frac(num2,den2)==reduce_frac(num,den):
                print(reduce_frac(num,den))



