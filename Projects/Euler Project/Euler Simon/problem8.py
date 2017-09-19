from time import time


def read_and_return():
    m = "".join(open("number_problem8").read().splitlines())
    return m


def main(big_number, length):
    temporary_product = 0
    for i in range(len(big_number) - length):
        product = 1
        for j in range(length):
            product *= int(big_number[i+j])
        if product > temporary_product:
            temporary_product = product
    return temporary_product


if __name__ == '__main__':
    t1 = time()
    result = main(big_number=read_and_return(), length=13)
    t2 = time()
    exit("Biggest Product: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
