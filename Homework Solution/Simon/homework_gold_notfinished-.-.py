def take_input_range():

    x = input("Give me your range...: ")
    try:
        x = int(x)
    except ValueError:
        pass

    return x


def primes(x):

    lst = []

    if x > 1:
        for j in range(2, x):
            for i in range(3, x, 2):
                if i % j == 0:
                    lst.append(int(i))

    return lst


def check_addition_true(x):

    lst = primes(x)

    for i in range(3, x):
        for j in lst:
            for k in lst:
                if j + k == i:
                    print(j, k, i)


def main():
    u = take_input_range()
    check_addition_true(u)

if __name__ == "__main__":
    main()
                             # do your homework next time lol ;) no jk just never give up ^^
                            # sorry man it isn't optimized at all.. gonna make a better version ;)