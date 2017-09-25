def contains_same_digits(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    if not len(str1) == len(str2):
        return False
    for i in range(0, len(str1)):

        if not str1.count(str1[i]) == str2.count(str1[i]):
            return False

    return True

not_found = True
num = 10
while not_found is True:
    correct = True
    mult = 2
    while contains_same_digits(num, num*mult) is True:
        print(num*mult)
        mult = mult + 1
    if mult > 6:
        print(num)
        break
    num += 1
    print(num)


print(contains_same_digits(1,2))