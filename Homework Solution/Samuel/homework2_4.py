def take_input():
    try:
        m = int(input("your first digit: "))
        n = int(input("your third digit: "))

    except ValueError:
        print("That was not an int!, try again.")
        return take_input()

    return m, n


def is_divisible(m, n):
    lst = []

    for x in range(1, 10):
        for y in range(1, 10):
            num = str(m) + str(x) + str(n) + str(y)

            if int(num) % 3 == 0:
                lst.append(num)

    return lst


def main():
    m, n = take_input()
    print(is_divisible(m, n))


if __name__ == '__main__':
    main()
