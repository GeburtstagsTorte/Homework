def take_input():

    x, y = input("give me the range of x, y which are gonna create an interval and put a space between: ").split()

    try:
        x, y = int(x), int(y)
    except ValueError:
        pass

    return x, y


def from_file():

    lst = []

    with open("file5") as f:
        f = f.readline().split()
        for i in f:

            try:
                i = int(i)
                lst.append(i)
            except ValueError:
                pass

    return lst


def check_whatever(lst, x, y):

    lst2 = []

    for i in lst:
        if i in range(x, y):
            lst2.append(i)

    return lst2[::-1]


def main():
    x, y = take_input()
    lst = from_file()
    print(check_whatever(lst, x, y))

if __name__ == "__main__":
    main()