def is_palindrome(num):
    text = str(num)
    if len(text) < 2:
        return False
    for i in range(0, int(len(text)/2)):
        if not text[i] == text[len(text)-1-i]:
            return False
    return True

lychrel_numbers = []

num = 1

while num < 10000:

    iterations = 1

    val = num
    val = val + int(str(val)[::-1])
    lychrel_numbers.append(num)
    while iterations < 50:

        if is_palindrome(val) is True:
            lychrel_numbers.remove(num)
            break
        val = val + int(str(val)[::-1])


        iterations += 1
    
    num += 1


print(len(lychrel_numbers))





