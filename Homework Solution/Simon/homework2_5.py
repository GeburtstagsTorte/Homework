def take_input():

    n = input("give me a number of your choice: ")

    try:
        n = int(n)
    except ValueError:
        return take_input()

    return n


def both_is_prime(x):

    def is_prime(x):
        for i in range(2, x//2):
            if x % i == 0:
                return False
        return True

    for i in range(2, x//2):
        if is_prime(x) and is_prime(x//10):
            return True
        else:
            return False


def numbers_in_n(n):

    lst = []

    for i in range(10**(n-1), 10**n):  
        if len(str(i)) == n and both_is_prime(i):
            lst.append(int(i))

    return lst


def main():
    u = take_input()
    print(numbers_in_n(u))

if __name__ == "__main__":
    main()