

def n_th_prime(n):
    lst = [3]
    while True:
        for i in range(lst[-1], lst[-1]**2, 2):
            if not any(i % x == 0 for x in lst):
                lst.append(i)
            if len(lst) > n-2:
                return lst[-1]


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = n_th_prime(10001)
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
