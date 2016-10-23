def homework(s):
    for x in range(2, s//2):
        for y in range(x, s//2):
            if x**2 + y**2 == s:
                print("your x is: ", x, "and your y is: ", y)


def input_nr():

    l = 0
    x = input("what is your k? ")

    try:
        x = int(x)
        l += x
    except ValueError:
        pass

    return l


def main():
    u = input_nr()
    homework(u)

if __name__ == "__main__":
    main()