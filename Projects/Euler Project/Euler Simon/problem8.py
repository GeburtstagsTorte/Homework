from time import time


def read_and_return():
    m = "".join(open("number_problem8").read().splitlines())
    return m


def main(length):
    number = read_and_return()
    temporary_product = 0
    for i in range(len(number) - length):
        product = 1
        for j in range(length):
            product *= int(number[i+j])
        if product > temporary_product:
            temporary_product = product
    return temporary_product


if __name__ == '__main__':
    t1 = time()
    result = main(13)
    t2 = time()
    exit("Biggest Product: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
