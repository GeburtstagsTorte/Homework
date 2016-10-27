def take_input():
    try:
        m, n = int(input("m = ")), int(input("n = "))
        return m, n
    except ValueError:
        return take_input()


def sum_digits(x):
    sum1 = 0
    while x != 0:
        sum1 += x % 10
        x //= 10
    return sum1


def print_numbers(m, n):
    count = 0
    for i in range(1, n*10):
        if sum_digits(i) <= m:
            print(i)
            count += 1
        if count == n:
            break


def main():
    m, n = take_input()
    print_numbers(m, n)

if __name__ == "__main__":
    main()
