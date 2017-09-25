def is_palindrome(text):
    end = len(text)
    for i in range(0, int(end/2)):
        if not text[i] == text[end-1-i]:
            return False
    return True


def binary_str(num):
    exp = 0 
    while 2**exp <= num:
        exp = exp + 1
    
    result = ""
    while exp > 0:
        exp = exp - 1
        mult = 2**exp
        if num - mult >= 0:
            result += "1"
            num = num - mult
        else:
            result += "0"
        

    return result
cumulative = 0
for i in range(0,999999):
    if is_palindrome(str(i)) is True and is_palindrome(binary_str(i)) is True:
        cumulative = cumulative + i
        print(i)
        

print(cumulative)
