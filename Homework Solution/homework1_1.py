def get_divisors(nr):

    st1 = set()

    for i in range(1, nr):
        if nr % i == 0:
            st1.add(i)

    return st1


def take_input():

    lst = []

    with open("file1") as f:
        x = f.readlines()
        x = x.split(" ")
        for i in x:
            try:
                i = int(i)
                lst.append(i)
            except ValueError:
                pass

    return lst


def common_divisors(st):

    final_set = set()

    for i in st:
        x = get_divisors(i)
        if len(final_set) < 1:
            final_set = x
        else:
            final_set = final_set & x

    return final_set


def main():
    u = take_input()
    print(common_divisors(u))


if __name__ == "__main__":
    main()