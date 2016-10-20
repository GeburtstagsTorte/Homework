def get_numbers():

    pos, neg = 0, 0
    with open("file3") as f:
        s = f.readline().split(" ")
        for x in s:
            try:
                x = int(x)
                if x < 0:
                    neg += 1
                elif x > 0:
                    pos += 1
            except ValueError:
                pass

    if pos > neg:
        return 1
    elif pos < neg:
        return -1
    else:
        return 0


def main():
    print(get_numbers())


if __name__ == "__main__":
    main()