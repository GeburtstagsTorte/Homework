

def n_th_prime(n):
    lst = [3]
    while True:
        for i in range(lst[-1], lst[-1]**2, 2):
            if not any(i % x == 0 for x in lst):
                lst.append(i)
            if len(lst) > n-2:
                return lst[-1]


def n_th_prime_v2(n):
    count = 1
    contender = 3
    while count < n-1:
        contender += 2
        if any(contender % i == 0 for i in range(3, int(contender**0.5)+1, 2)):
            continue
        count += 1
    return contender


if __name__ == '__main__':
    from time import time

    t1 = time()
    result = n_th_prime_v2(10001)
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))


