from itertools import permutations
perms = [''.join(p) for p in permutations('1234567890')]

def follows_property(num_text):
    divi = [1,2,3,5,7,11,13,17]
    for i in range(1,len(divi)):
        num = int(num_text[i:i+3])
        if not num % divi[i] == 0:
            return False
    return True

total = 0
for perm in perms:
    if perm[0] == "0":
        pass
    elif follows_property(perm) is True:
        total += int(perm)
print(total)