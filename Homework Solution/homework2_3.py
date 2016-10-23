def take_input():

    m, n = input("give me m, n and put a space between: ").split(" ")
    try:
        m, n = int(m), int(n)
        return m, n
    except ValueError:
        pass


def sum_of_digits(n):

    n = str(n)
    n1 = 0

    for i in n:
        n1 += int(i)

    return n1


def compare_m_n(m, n):

    lst = []

    for i in range(1, n*10):   # may +1 cuz task? # no! need for n to be a greater range....
        if sum_of_digits(i) <= m:      # fml no lol i tricked myself haha
            lst.append(i)

    return lst[:n]


def main():
    m, n = take_input()
    print(compare_m_n(m, n))

if __name__ == "__main__":
    main()