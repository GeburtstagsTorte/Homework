# What is the value of the first triangle number to have over five hundred divisors?
from itertools import chain


def factorise(n):
    l = []
    for i in chain([2], range(3, n//2 + 1, 2)):
        while n % i == 0:
            l.append(i)
            n = n // i
        if i > n:
            break
    return l


def counter(l):
    count = 1
    lst = []
    total = 1
    for i in range(len(l)):
        try:
            if l[i] == l[i+1]:
                count += 1
            else:
                lst.append((i, count))
                total *= count + 1
                count = 1
        except IndexError:
            lst.append((i, count))
            total *= count + 1
            count = 1
            pass
    return total


def main():
    from time import clock

    total = 1
    n = 31
    sum = (n*(n+1)) // 2
    t1 = clock()
    while total < 500:
        n += 1
        sum = (n * (n + 1)) // 2
        l = factorise(sum)
        total = counter(l) if counter(l) > total else total
    t2 = clock()
    print(sum)
    print(t2-t1)

if __name__ == '__main__':
    main()
