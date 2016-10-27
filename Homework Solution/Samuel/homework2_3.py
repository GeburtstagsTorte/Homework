import re


def take_input():
    try:
        n = int(input("how many numbers do you want?: "))
        m = int(input("sum boundary: "))

    except ValueError:
        print("That was not an int!, try again.")
        return take_input()

    return n, m


def equal_sum(n, m):
    lst = []
    num = 1
    count = 0

    while len(lst) < n:
        num = str(num)
        for char in num:
            count += int(char)

        if count <= m:
            lst.append(num)

        num = int(num) + 1
        count = 0
    return lst


def main():
    n, m = take_input()
    print(equal_sum(n, m))


if __name__ == "__main__":
    main()
