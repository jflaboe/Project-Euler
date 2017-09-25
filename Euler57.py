from fractions import Fraction
def is_prime(num):

    if num < 2:
        return False
    
    if num < 4:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num**(0.5) + 1)):

        if num % i == 0:
            
            return False
    
    return True

def prime_factors(num):

    if num < 2:
        return [num]

    if is_prime(num):

        return [num]

    div = 2

    while True:
        if num % div == 0:
            return prime_factors(div) + prime_factors(num/div)
        div += 1


def list_mult(nums):
    prod = 1
    for num in nums:
        prod*=num
    return prod

expansion = 2
count = 0
frac = 1/(2 + Fraction(1/2))

while expansion < 1000:
    
    expansion += 1
    frac = 1/(2+frac)
    val = 1 + frac

    if len(str(val.numerator)) > len(str(val.denominator)):
        count += 1

print(count)
        

