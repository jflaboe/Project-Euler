def count_triangles(perimeter):
    a = 3
    
    count = 0
    while a < perimeter/3:
        b = a
        c = perimeter - a - a
        while a**2 + b**2 < c**2:
            b += 1
            c = perimeter - a - b
        if a**2 + b**2 == c**2:
            count += 1
        a += 1
    return count


max_sol = 0
max_p = 0

for i in range(12, 1000):
    count = count_triangles(i)
    if count > max_sol:
        max_sol = count
        max_p = i

print(max_p)