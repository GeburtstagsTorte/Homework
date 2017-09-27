import math


def generate_primes_below(n):
    # doesnt work yet
    lst = [3]
    while True:
        for i in range(lst[-1], lst[-1]**2, 2):
            if not any(i % x == 0 for x in lst if not x > int(math.sqrt(i))):
                lst.append(i)
            elif lst[-1] > n:
                return lst[:len(lst)-1]


def generate_primes_below_v2(n):
    primes = [2]
    for i in range(3, n, 2):
        if not any(i % j == 0 for j in range(2, round(math.sqrt(i)+1))):
            primes.append(i)
    return sum(primes)


def generate_primes_below_v3(n):
    y = list(range(2, int(n)))
    while len(y) > 0 and y[0] < int(math.sqrt(n)):
        yield y[0]
        y = [x for x in y if x % y[0]]
    for x in y:
        yield x


def generate_primes_below_v4(n):
    # INTERESTING

    # using sieve of eratosthenes
    isPrimes = [True] * n
    isPrimes[0] = False
    isPrimes[1] = False
    for i, v in enumerate(isPrimes):
        if not v:
            # i is not a prime => skip
            continue
        # multiples of i except i are non primes
        for k in range(i + i, n, i):
            isPrimes[k] = False
    # collect primes and sum primes
    primes = [i for i, v in enumerate(isPrimes) if v]
    return sum(primes)


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = generate_primes_below_v4(int(2E6))  # sum(generate_primes_below_v3(2E6))
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
