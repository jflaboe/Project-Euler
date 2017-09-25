def one_cent_ways(balance):
    return 1

def two_cent_ways(balance):
    return(int(balance/2) + 1)

def five_cent_ways(balance):
    max_amount = int(balance/5)
    count = 0
    for i in range(0, max_amount+1):
        count += two_cent_ways(balance - 5*i)
    return count

def ten_cent_ways(balance):
    max_amount = int(balance/10)
    count = 0
    for i in range(0, max_amount+1):
        count+=five_cent_ways(balance-10*i)
    return count

def twenty_cent_ways(balance):
    max_amount = int(balance/20)
    count = 0
    for i in range(0, max_amount+1):
        count+=ten_cent_ways(balance-20*i)
    return count

def fifty_cent_ways(balance):
    max_amount = int(balance/50)
    count = 0
    for i in range(0, max_amount+1):
        count+=twenty_cent_ways(balance-50*i)
    return count
    
def hundred_cent_ways(balance):
    max_amount = int(balance/100)
    count = 0
    for i in range(0, max_amount+1):
        count+=fifty_cent_ways(balance-100*i)
    return count

def two_hundred_cent_ways(balance):
    max_amount = int(balance/200)
    count = 0
    for i in range(0, max_amount+1):
        count+=hundred_cent_ways(balance-200*i)
    return count


print(two_hundred_cent_ways(200))
