from time import clock
from math import sqrt


def euler7():
    time1 = clock()

    primes = [2]
    candidate = 3

    while len(primes) <= 10000:

        for i in primes:
            if candidate % i == 0:
                candidate += 2
                break
        else:
            primes.append(candidate)
            candidate += 2

    time2 = clock()
    print("euler7 ver 1: ", primes[len(primes)-1])
    print("euler7 ver 1 time: ", time2-time1, "sec.")


def euler7ver2():
    primes = [2]
    time1 = clock()
    candidates = [i for i in range(1, 100000, 2)]
    # optimize code by localize limit from range
    for i in candidates:
        if sqrt(i) in candidates:
            candidates.remove(i)

    for i in candidates:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    time2 = clock()
    print("euler7 ver2 number: ", primes[10001 + 1])
    print("euler7 ver2: ", primes[len(primes)-1])
    print("euler7 ver2 length: ", len(primes))
    print("euler7 ver2 time: ", time2-time1, "sec.")


def euler7ver_pro():
    time1 = clock()

    def is_prime(x):
        for i in range(3, int(x/2), 2):
            if x % i == 0:
                return False
        return True

    prime = 3
    count = 2
    while count < 10001:
        prime += 2
        if is_prime(prime):
            count += 1

    time2 = clock()
    print("(vlad version) number: ", prime)
    print("(vlad version) time: ", time2-time1)

euler7ver2()