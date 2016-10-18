def is_divisor(st):

    i = st
    st1 = set([])

    for x in range(1, i):     #this is so hard man... my brain aches
        if i % x == 0:
            st1.add(x)
            st1.add(i)
        else:
            pass
    print(st)
    return st1


def take_input():

    lst = []

    with open("file1") as f:
        x = f.readline()
        x = x.split(" ")
        for i in x:
            try:
                i = int(i)
                lst.append(i)
            except ValueError:
                pass

    return lst


def common_divisors(st):

    final_set = set([])

    for i in st:
        x = is_divisor(i)
        for i in x:
            final_set.add(i)
    return final_set


def main():
    u = take_input()
    print(common_divisors(u))


if __name__ == "__main__":
    main()