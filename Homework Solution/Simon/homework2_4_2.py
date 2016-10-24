def all_funcs():

    m, n = input("give me m and n and put a space between: ").split()
    lst = []
    finalstr = ""

    for i in range(10):
        for j in range(10):
            num = m + str(i) + n + str(j)
            lst.append(int(num))

    for i in lst:
        if i % 3 == 0:
            finalstr += str(i) + ", "

    return finalstr

print(all_funcs())