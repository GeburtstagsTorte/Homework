def take_input():

    m, n = input("give me m, n with a space between").split()
    try:
        m, n = int(m), int(n)
        return str(m), str(n)
    except ValueError:
        pass


def take_string(m, n):

    num = ""
    nums = []
    # p = int(m + "000") % 3

    try:
        for i in range(10):
            for j in range(10):
                num += m + str(i) + n + str(j)
                if manipulate(num):
                    nums.append(num)
                num = ""     # haha that took me a minute lol (but i print debugged ;))(printed longer and longer numbers)
    except ValueError:
        pass

    return nums


def manipulate(num):  # find name

    try:
        num = int(num)
        if num % 3 == 0:
            return num
    except ValueError:
        pass

    # bad approach
    """for i in lst:
        if i % 3 == 0:
            lst.append(i)

    return lst2"""


def main():
    m, n = take_input()
    print(take_string(m, n))

if __name__ == "__main__":
    main()
