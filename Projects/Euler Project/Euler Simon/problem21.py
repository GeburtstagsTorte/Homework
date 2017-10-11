

def yield_divisors(number):
    for i in range(1, number//2 + 1):
        if number % i == 0:
            yield i


def main(n):
    amicable = 0

    for i in range(n):
        x = sum(yield_divisors(i))
        y = sum(yield_divisors(x))
        if y == i and x < i:
            amicable += i + x

    return amicable


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = main(10000)
    t2 = time()
    exit("Result: {}\nTime: {} ms".format(result, (t2 - t1) * 1000))
