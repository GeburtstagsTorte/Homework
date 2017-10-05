

def read_and_return():
    m = open("numbers_problem13").read().splitlines()
    print(m)
    return m


def main(numbers):
    return str(sum([int(x) for x in numbers]))[:10]


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = main(read_and_return())
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
