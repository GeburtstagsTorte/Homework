def take_input():
    try:
        n = int(input("how many digits?: "))

    except ValueError:
        print("That was not an int!, try again.")
        return take_input()

    return n


def prim(n):
    primes = [2]

    for x in range(3, 10**n - 1, 2):
        for i in primes:
            if x % i == 0:
                break

        else:
            primes.append(x)

    return primes


def is_prime_in_prime(primes, n):

    little_primes = [x for x in primes if x < 10]
    l = []

    for x in primes:
        num = str(x)

        for char in num:
            if int(char) in little_primes and len(num) == n:
                l.append(num)
                break

    return l


def main():
    n = take_input()
    primes = prim(n)
    print(is_prime_in_prime(primes, n))


if __name__ == '__main__':
    main()
