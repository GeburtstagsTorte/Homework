def take_input():
    x = input("Please type a number: ")
    try:
        x = int(x)
    except ValueError:
        #return take_input()
        pass
    print(x)
    return x


def return_list(x):
    lst = []
    for i in range(1, x+1):
        for j in range(i):
            lst.append(i)
    return lst[:x]


def main():
    u = take_input()
    print(return_list(u))


if __name__ == "__main__":
    main()