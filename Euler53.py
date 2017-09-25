import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

count = 0
for i in range(23, 101):
    r = 2
    while ncr(i, r) < 1000000:
        r = r + 1
    other_end = i - r

    count += other_end - r + 1
print(count)