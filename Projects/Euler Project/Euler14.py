# Collatz sequence: Which starting number, under one million, produces the longest chain?
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1


def collatz_algorithm(n):
    count = 0
    while n != 1:
        if not n % 2:
            n //= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count


def main():
    from time import clock
    longest = 0
    num = int()
    t1 = clock()
    n = 1
    while n < 1000000:
        trail = collatz_algorithm(n)
        if trail > longest:
            longest = trail
            num = n
        n += 2
    t2 = clock()
    print(num)
    print(t2-t1)


if __name__ == '__main__':
    main()
