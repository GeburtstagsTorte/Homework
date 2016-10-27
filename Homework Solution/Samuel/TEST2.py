import re


def file_input():

    with open("test2 file", "r") as f:
        s = re.findall('[-\d]+', f.read())

    return s


def user_input():
    try:
        x = int(input("first interval boundary: "))
        y = int(input("second interval boundary: "))
    except ValueError:
        print("Not an int! Try again.")
        return user_input()
        # don't know and can't find any other way to handle this.

    return x, y


def is_in_interval(s, interval):
    interval = sorted(interval)
    lst = []

    for i in s[::-1]:
        if interval[0] < int(i) < interval[1]:
            lst.append(i)

    return lst


def is_in_interval_v2(s, interval):
    # second version just for fun
    interval = sorted(interval)
    lst = [x for x in s if interval[0] < int(x) < interval[1]]

    return lst[::-1]


def main():
    u = file_input()
    v = user_input()

    print(is_in_interval(u, v))
    print(is_in_interval_v2(u, v))


if __name__ == "__main__":
    main()
