def get_num():
    n = open("euler13").read().splitlines()
    n = [i for i in n]
    c = 0
    for i in n:
        c += int(i)
    print(c)

get_num()