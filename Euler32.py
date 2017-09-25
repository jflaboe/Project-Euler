from itertools import permutations
perms = [''.join(p) for p in permutations('123456789')]

def pan_products(num_string):
    result = []
    product = int(num_string[5:])

    for i in range(1,4):
        if int(num_string[:i])*int(num_string[i:5])==product:
            return [product]
    return result

prods = []
for i in range(0,len(perms)):
    prods = prods + pan_products(perms[i])

print(sum(list(set(prods))))
    

