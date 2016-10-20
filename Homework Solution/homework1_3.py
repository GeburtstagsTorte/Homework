def get_numbers():

    lst = []

    with open("file3") as f:
        s = f.readline()
        s = s.split(" ")
        for x in s:
            try:
                x = int(x)
                lst.append(x)
            except ValueError:
                pass

    return lst


def what_is_more(lst): #sorry for noob name lol

    pos = 0
    neg = 0

    for i in lst:
        if i > 0:
            pos += 1
        if i < 0:
            neg += 1
        if i == 0:
            pass

    if pos > neg:
        return 1
    if neg > pos:
        return -1
    if neg == pos:
        return 0


def main():
    u = get_numbers()
    print(what_is_more(u))


if __name__ == "__main__":
    main()