import math

def find_factors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            factors += [int(i), int(num/i)]

    factors = list(set(factors))
    return factors

def is_abundant(num):
    factors = find_factors(num)
    if sum(factors) > 2*num:
        return True
    return False

def can_be_summed(num, list_of_num):
    for i in range(0, int(num/2.0 + 1)):
        if i in list_of_num:
            if num-i in list_of_num:
                return True

    return False


print(find_factors(12))
print(find_factors(28))

print(is_abundant(12))
print(is_abundant(28))

abundant_num = []
cannot_be_summed =[]


for i in range(1,28123):
    if i%1000 == 0:
        print(i)
    if is_abundant(i) is True:
        abundant_num.append(i)

    if can_be_summed(i, abundant_num) is False:
        cannot_be_summed.append(i)

print(sum(cannot_be_summed))


    

