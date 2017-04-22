from time import clock
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# D:\#PRGM\Python\Euler Project\euler8.txt


def euler8():
    time1 = clock()
    f = open("D:\#PRGM\Python\Euler Project\euler8.txt", "r")
    count = 1
    max_value = 0
    n = 14
    try:
        candidates = f.read()
        while n < len(candidates):

            for i in candidates[n-13:n]:
                count *= int(i)
            if count > max_value:
                max_value = count
                count = 1
                n += 1
            else:
                count = 1
                n += 1
        time2 = clock()

        t = time2-time1
        print("v1:")
        print(max_value)
        print(t, "sec.")

    finally:
        f.close()
        return t


def euler8ver2():
    time1 = clock()
    f = open("D:\#PRGM\Python\Euler Project\euler8v2.txt", "r")
    count = 1
    max_value = 0
    n = 14
    try:
        candidates = f.read()
        candidates = candidates.replace('\n', "")
        while n < len(candidates):

            for i in candidates[n-13:n]:
                count *= int(i)
            if count > max_value:
                max_value = count
                count = 1
                n += 1
            else:
                count = 1
                n += 1
        time2 = clock()

        t = time2-time1
        print("v2:")
        print(max_value)
        print(t, "sec.")

    finally:
        f.close()
        return t


def time(t1, t2):
    print("difference: ", abs(t1-t2), "sec.")
    print("ratio (v1 / v2)", (t1/t2))

time(euler8(), euler8ver2())
