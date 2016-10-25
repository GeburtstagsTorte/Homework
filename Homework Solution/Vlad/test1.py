a = open("test1").read().splitlines()[0].split(" ")
lst, val = [i for i in range(1, len(a)+1)], [0 for i in range(1, len(a)+2)]
for i in a:
    if int(i) in lst:
        val[int(i)] += 1
    else:
        print("False")
        break
else:
    for i in range(1, len(a) + 1):
        if val[i] != 1:
            print("False")
            break
    else:
        print("True")