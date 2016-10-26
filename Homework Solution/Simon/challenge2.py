def take_input():

    x, y = input("give me the range of x, y which are gonna create an interval and put a space between: ").split()

    try:
        x, y = int(x), int(y)
    except ValueError:
        pass
    # This will cause an error if its not an int (x or y)
    return x, y


def from_file():
    # This wil only work if nothing than a space is between but that's not the point 
    lst = []

    with open("file5.txt") as f:
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
            # if x is higher than y nothing happens, users are dumb
            lst2.append(i)

    return lst2[::-1]


def main():
    x, y = take_input()
    lst = from_file()
    print(check_whatever(lst, x, y))

if __name__ == "__main__":
    main()
