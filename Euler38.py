from itertools import permutations
perms = [''.join(p) for p in permutations('123456789')]


def can_be_created(num_text):
    for i in range(1,5):
        initial = num_text[:i]
        remaining = num_text[i:]
        n = 1
        while True:
            n = n + 1
            new_text = str(int(initial)*n)
            if len(new_text) > len(remaining):
                break
            
            if not new_text == remaining[0:len(new_text)]:
                break
            
            remaining = remaining[len(new_text):]

            if len(remaining) == 0:
                return True
    return False
            

perms.sort()

for i in range(0, len(perms)):
    if can_be_created(perms[len(perms)-1-i]):
        print(perms[len(perms)-1-i])
        break
