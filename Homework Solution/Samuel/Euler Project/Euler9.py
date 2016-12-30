# a + b + c = 1000; a < b < c a; a² + b² = c²; a,b,c element N
# l = [(a, b, c) for a in range(1, 100) for b in range(a, 100) for c in range(b, 100) if a*a + b*b == c*c]

from math import sqrt
from time import clock


def get_squared():
    l = [i**2 for i in range(2, 1000)]
    return l


def get_triplet():
    t1 = clock()
    l = get_squared()
    for i in range(len(l)):
        for j in range(i, len(l)):
            n = l[i] + l[j]
            for k in l[j::]:
                if n == k and int(1000 - sqrt(l[i]) - sqrt(l[j]) - sqrt(k)) == 0:
                    print(sqrt(l[i])*sqrt(l[j])*sqrt(k))
                    t2 = clock()
                    print(t2-t1)
                    break


def problem(p=1000):
    t1 = clock()
    m = int(sqrt(p / 2))
    n = (p // 2 - m**2)
    while n % m != 0 and m > 1:
        m -= 1
        n = (p // 2 - m**2)
    n //= m
    if not m > n:
        return None
    t2 = clock()
    print(t2-t1)
    return (m**2 - n**2)*(2*n*m)*(m**2 + n**2)


def main():
    print(problem())
    get_triplet()

if __name__ == '__main__':
    main()
