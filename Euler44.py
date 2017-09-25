import math
def penta(n):
    return int(n*(3*n-1) / 2)
penta_list = [penta(n) for n in range(1,11)]
count = 10
print(penta_list)

def is_penta(n):
    inverse = (math.sqrt(24*n+1) + 1)/6
    return int(inverse) == inverse

print(is_penta(5))
print(is_penta(6))
print(is_penta(15))
print(is_penta(22))

mid = 1
found_best = False

while True:
    mid = mid + 1
    low = 1
    if found_best is True:
        break
    
    while low < mid:
        p_low = penta(low)
        p_mid = penta(mid)
        p_high = p_low + p_mid
        if is_penta(p_high) is True:
            p_sum = p_high + p_low
            if is_penta(p_sum) is True:
                found_best = True
                print(p_mid)
        low = low + 1
    
        