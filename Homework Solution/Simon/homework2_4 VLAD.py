def take_input():
    try:
        m, n = int(input("m = ")), int(input("n = "))
        return m, n
    except ValueError:
        return take_input()


def build_number(m, x, n, y):
    return m * 10**3 + x * 10**2 + n * 10 + y


def construct_numbers(m, n):
    for i in range(0, 10):
        for j in range(0, 10):
            nr = build_number(m, i, n, j)
            if nr % 3 == 0:
                print(nr)


def main():
    m, n = take_input()
    construct_numbers(m, n)

if __name__ == "__main__":
    main()